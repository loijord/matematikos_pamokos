import laspy
from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy_indexed as npi
import numpy as np
import pptk
import os
from collections import defaultdict
from tqdm import tqdm
from itertools import chain
import pandas as pd

class Cubeview:
    X = np.array([[[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]],
                  [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
                  [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
                  [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
                  [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
                  [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]).astype(float)

    def __init__(self, cubes_xyz=[], size_info=(1, 1, 1), translate_info=(0, 0, 0)):
        self.cubes_xyz = cubes_xyz  # cube indexes estimated to be np.arrays
        self.size_info = size_info  # their size
        self.translate_info = translate_info  # their starting position
        self.event_handle = False

    @staticmethod
    def vectorised_sum(a,b): return np.array([np.sum([a,n],axis=0) for n in b])

    @staticmethod
    def vectorised_prod(a, b): return np.array([np.prod([a, n], axis=0) for n in b])

    @staticmethod
    def _fix_view(scalefactor=1.5, ax=None):
        bbox = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        bbox_center = np.mean(bbox, axis=1)
        bbox_dim = np.max(bbox, axis=1) - np.min(bbox, axis=1)
        scaling_factors = scalefactor * bbox_dim / np.max(bbox_dim)
        tr1, tr2, tr3 = bbox_center
        s1, s2, s3 = scaling_factors
        A = np.array([[1, 0, 0, -tr1], [0, 1, 0, -tr2], [0, 0, 1, -tr3], [0, 0, 0, 1]])
        T = np.array([[s1, 0, 0, 0], [0, s2, 0, 0], [0, 0, 2 * s3, 0], [0, 0, 0, 1]])
        B = np.array([[1, 0, 0, tr1], [0, 1, 0, tr2], [0, 0, 1, tr3], [0, 0, 0, 1]])
        ax.get_proj = lambda: np.dot(np.dot(np.dot(Axes3D.get_proj(ax), B), T), A)

    def add_preview(self, fig=None, block=True, closing=True):
        if fig is None:
            raise AttributeError('fig parameter required')
        def onclose(event): fig.canvas.stop_event_loop()
        fig.show()
        if block:
            fig.canvas.mpl_connect('close_event', onclose)
            fig.canvas.start_event_loop()
        if closing: plt.close(fig)

    def cuboid_data(self):
        translation = self.cubes_xyz.min(axis=0)  # translation vector of cube
        translated_locii = self.cubes_xyz - translation  # every cube is pushed so that its corner stands at (0,0,0)
        scaled_locii = translated_locii * self.size_info
        extended_locii = self.translate_info + scaled_locii
        data = self.vectorised_sum((self.X + translation) * self.size_info,  extended_locii)
        return data

    def set_lims(self, mode='fitted', ax=None, on_last=False):
        if on_last:
            lim0 = np.min(ax.collections[-1]._vec[:3], axis=1)
            lim1 = np.max(ax.collections[-1]._vec[:3], axis=1)
        else:
            lim0 = np.min(np.array([np.min(pc._vec[:3], axis=1) for pc in ax.collections]), axis=0)
            lim1 = np.max(np.array([np.max(pc._vec[:3], axis=1) for pc in ax.collections]), axis=0)
        bound = lim1 - lim0
        if mode == 'normal':
            (xlim, ylim, zlim) = zip(lim0, lim0 + np.repeat(np.max(bound), 3))
        if mode == 'fitted':
            (xlim, ylim, zlim) = zip(lim0, lim0 + bound)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_zlim(zlim)

    def voxplot(self, facecolors, edgecolors='none', labels=None, ax=None, mode = 'fitted', fontsize=18, textcolor='#999999', focus=False, zorder=1):
        data = self.cuboid_data()
        pc = Poly3DCollection(np.concatenate(data), facecolors=np.repeat(facecolors, 6, axis=0),
                                edgecolors=np.repeat(edgecolors, 6, axis=0), zorder=zorder)
        ax.add_collection3d(pc)
        self.set_lims(mode=mode, ax=ax, on_last=focus)
        if labels is not None:
            positions = iter(np.mean(data[:,-1,:,:], axis=1))
            for n in labels: ax.text(*next(positions), n, zorder=100, fontsize=fontsize, color=textcolor)
        self._fix_view(ax=ax)
        return self.get_focus(ax=ax)

    def get_focus(self, ax=None): return (ax.get_xlim(), ax.get_ylim(), ax.get_zlim())

    def set_focus(self, fc, ax=None):
        ax.set_xlim(fc[0])
        ax.set_ylim(fc[1])
        ax.set_zlim(fc[2])
        self._fix_view(ax=ax)

    def wait_for_event(self, event, koef=15, ax=None, fig=None):
        if event.key in ["up", "down", "right", "left", "ctrl+down", "ctrl+up"]:
            # taken from https://github.com/matplotlib/matplotlib/issues/110
            ax.autoscale(enable=False, axis='both')  # I have no idea, it this line have some effect at all
            ## Set nearly similar speed of motion in dependency on zoom
            xkoef = (ax.get_xbound()[0] - ax.get_xbound()[1]) / koef
            ykoef = (ax.get_ybound()[0] - ax.get_ybound()[1]) / koef
            zkoef = (ax.get_zbound()[0] - ax.get_zbound()[1]) / koef
            if event.key == "up":
                ax.set_ybound(ax.get_ybound()[0] + xkoef, ax.get_ybound()[1] + xkoef)
            elif event.key == "down":
                ax.set_ybound(ax.get_ybound()[0] - xkoef, ax.get_ybound()[1] - xkoef)
            elif event.key == "right":
                ax.set_xbound(ax.get_xbound()[0] + ykoef, ax.get_xbound()[1] + ykoef)
            elif event.key == "left":
                ax.set_xbound(ax.get_xbound()[0] - ykoef, ax.get_xbound()[1] - ykoef)
            elif event.key == "ctrl+down":
                ax.set_zbound(ax.get_zbound()[0] - zkoef, ax.get_zbound()[1] - zkoef)
            elif event.key == "ctrl+up":
                ax.set_zbound(ax.get_zbound()[0] + zkoef, ax.get_zbound()[1] + zkoef)
            fig.canvas.draw()
        else:
            self.event_handle = event.key
            fig.canvas.stop_event_loop()


class PointcloudScientist():
    def __init__(self, points, ids=None, translate_info=(0, 0, 0), size_info=(50, 50, 50)):
        self.points = points #this is full-format data read from lidar; it is always immutable
        self.ids = ids #this is ids of points desired on this cubecloud

        if ids is None: self.ids = np.arange(len(self.points)) #we desire all the pointcloud by default; 0.1s for arange(27M)

        t=time(); print('   ...preparation (iteration through given ids of points, if any): ', end='')
        # do we create a copy of self.points or use iteration to make subset of them:
        if ids is None: self.npoints = self.points  # copy if we require all ids
        else: self.npoints = self.points[self.ids]  # iterate otherwise (cus iteration is expensive)
        print(round(time() - t, 3))

        self.translate_info = translate_info
        self.size_info = size_info
        self.cubes = None
        self.cube_slices = None

    @staticmethod
    def group_by(array1, array2):
        keys, values = npi.group_by(array1, values=array2)
        keys_totuples = ((n[0], n[1], n[2]) for n in keys)  # [tuple(n) for n in keys]
        return dict(zip(keys_totuples, values))

    def find_cubes(self, connect_database=True):
        # making dictionary with keys that are 3D indexes of cubes and
        # values are corresponding ids of points of these cubes
        if self.cubes is not None: raise ValueError('cubes already found')
        else:
            PATH = 'cubesplit '+str((self.translate_info, self.size_info))
            if connect_database and PATH in os.listdir():
                print('   ...retrieving grouping [from database =', PATH, ']:')
                cubescientist = CubeScientist()
                cubescientist.retrieve_cubes(PATH)
                if os.listdir(PATH) == []: raise ValueError('houston, we''ve got an empty database')
                self.cubes, self.cube_slices = cubescientist.cubes, cubescientist.cube_slices
            else:
                t=time(); print('   ...slicing (calculating indexes of cubes):', end='')
                self.cube_slices = np.array([(self.npoints['X'] - self.translate_info[0]) // self.size_info[0],
                                   (self.npoints['Y'] - self.translate_info[1]) // self.size_info[1],
                                   (self.npoints['Z'] - self.translate_info[2]) // self.size_info[
                                       2]]).T  # integral slice indexes, assuming startpoit is given in translate_info
                print(round(time() - t, 3))
                t=time(); print('    grouping with pandas[new]:', end='')
                self.cubes = pd.DataFrame(self.cube_slices).groupby([0,1,2], as_index=True).indices
                print(round(time() - t, 3))
                if connect_database:
                    t = time(); print('   ...saving[new]:', end='')
                    os.mkdir(PATH)
                    cubescientist = CubeScientist(self.cubes)
                    if connect_database: cubescientist.save_cubes(PATH, 'cubes_with')

    #extract points
    #self.cubecloud.points[self.cubecloud.cubes[upmost_node]][['X', 'Y', 'Z']]

    def clone_fromcubes(self, suitable_cubes):
        # creates new instance, getting point ids from cubes; suitable_cubes must be subset of self.cubes
        # DISCLAIMER: please be sure that :
                #your suitable cubes is really a sunset of self.cubes;
                #your self.cubes is not None
        # DISCLAIMER2: I assume copy of cube_slices parameter is not needed until
        cubecloud = PointcloudScientist(self.points)
        cubecloud.translate_info = self.translate_info
        cubecloud.size_info = self.size_info
        cubecloud.cubes = {cube: self.cubes[cube] for cube in suitable_cubes}
        self.ids = npi.union(self.cubes.values())
        return cubecloud

    def clone_frompoints(self, collection): #from collection like [np.array([1,4]), np.array([8,9])]
        # joining points from all the collections
        if len(collection) > 0:
            clovercloud = PointcloudScientist(self.points, ids=npi.union(*collection), size_info = self.size_info, translate_info = self.translate_info)
        else:
            clovercloud = PointcloudScientist(self.points, ids=[], size_info = self.size_info, translate_info = self.translate_info)
        if len(collection) > 0:
            clovercloud.find_cubes(connect_database=False)
        else: clovercloud.cubes = {}
        return clovercloud

    def plotfast(self, cubes):
        #assuming pptk needs preserve cubes that has ids, we create new cubecloud instantly with no wories
        clovercloud = self.clone_frompoints([self.cubes[n] for n in cubes])
        self.plot3d(selected=clovercloud)

    def plot3d(self, selected=None, interaction=True):
        def get_new_ids():
            return v.get('selected')

        def get_new_cubes(selected_ids):
            return {loaded_cubes[id]: self.cubes[loaded_cubes[id]] for id in selected_ids}

        def get_selection_ids(loaded_cubes, selected_cubes):
            return [i for i in range(len(loaded_cubes)) if loaded_cubes[i] in selected_cubes]

        def matplot(selected_cubes):


            points_in_selected_cubes = [list(self.points[point_ids][['X', 'Y', 'Z']]) for point_ids in
                                        selected_cubes.values()]
            xdata, ydata, zdata = list(zip(*list(chain.from_iterable(points_in_selected_cubes))))

            fig = plt.figure('Composed element')
            ax = fig.gca(projection='3d')
            vxv = Cubeview(np.array(list(selected_cubes.keys())), size_info=self.size_info, translate_info=self.translate_info)
            vxv.voxplot(ax=ax, facecolors='#80800030', edgecolors='grey')
            #vxv.fix_view(ax=ax)
            #vxv.voxplot(ax=ax, facecolors='olive', edgecolors='grey')
            plt.show()

        if self.cubes is None: self.find_cubes()
        loaded_cubes = list(self.cubes)
        v = pptk.viewer(loaded_cubes)
        v.set(point_size=0.2)
        inp = 'inception'
        while inp != 'quit':
            if (
                    inp == 'new' or inp == 'inception') and selected is not None:  # if nothing is selected, wait for selection and feed this to a subdict
                print('Restarting initial selection:..', end='')
                selection_of_loaded_cubes = get_selection_ids(loaded_cubes, selected.cubes)
                v.set(selected=selection_of_loaded_cubes)
                print('.done.')
            if inp[:3] == 'inv':
                if bool(inp[3:].replace(' ', '')):
                    dst = int(inp[3:])
                else:
                    dst = 1
                print('inverting selection for dst=', dst, '..', end='')
                t = time()
                selected_ids_new = get_new_ids()
                selected_cubes_new = get_new_cubes(selected_ids_new)
                init_cubes = selected_cubes_new.copy()  # initially selected cubes
                for loop in range(dst):
                    # asking neighbours which cubes can be selected
                    neighbours_of_selected_cubes = [
                        [(n[0], n[1], n[2] + 1), (n[0], n[1], n[2] - 1), (n[0], n[1] + 1, n[2]), \
                         (n[0], n[1] - 1, n[2]), (n[0] + 1, n[1], n[2]), (n[0] - 1, n[1], n[2])] for n in
                        selected_cubes_new]
                    union_of_neighbours = list(set(list(chain.from_iterable(neighbours_of_selected_cubes))))
                    selected_cubes_new = [n for n in union_of_neighbours if n in loaded_cubes]
                    selected_ids_new = get_selection_ids(loaded_cubes, selected_cubes_new)
                    selected_cubes_new = get_new_cubes(selected_ids_new)
                # filtering out initially selected cubes
                selected_cubes_new = [n for n in union_of_neighbours if n not in init_cubes]
                selected_ids_new = get_selection_ids(loaded_cubes, selected_cubes_new)

                v.set(selected=selected_ids_new)
                print(time() - t)

            print('Select your cubes in pptk or type ENTER to finish')
            v.wait()
            selected_ids_new = get_new_ids()
            selected_cubes_new = get_new_cubes(selected_ids_new)

            if not(interaction):
                if len(selected_ids_new) == len(selection_of_loaded_cubes):
                    v.close()
                    break

            print('Plotting selected cubes. Close tkinter to continue..', end='')
            matplot(selected_cubes_new)
            #inp='quit'

            '''print('.done. Type ''enter/new/quit/inv'' ')
            inp = input()'''
        v.close()



class CubeScientist:
    def __init__(self, cubes = None, metrics=None):
        """performs essential operations of cubes, they are hashed and input is dictionary only"""
        self.cubes = cubes #guess its not important if cubes are dict or list
        self.metrics = metrics
        self.shape_archive = defaultdict()

    def is_bipartialy_connected(self, other_scientist, max_hits=2): #return Falses or element for each n in other_scientist
        if self.metrics not in ['taxicab_search']: raise TypeError
        return self.metrics.vector_on_vector(self.cubes, other_scientist.cubes, take=max_hits) is not False

    def connected_dict(self, shape, on_cubes=None): #returns dictionary form of connecting cubes
        if self.metrics.name not in ['taxicab_search_3d']: raise TypeError
        if on_cubes is None: on_cubes = self.cubes
        #if shape not in self.shape_archive:
        taxicab_neigbours = self.metrics.vector_on_vector(self.cubes, on_cubes, shape=shape) #generator of generators
        corresponding_neighbourhoods = map(lambda x: list(x), taxicab_neigbours)
        dict_representation = dict(zip(on_cubes, corresponding_neighbourhoods))
        #self.shape_archive[shape] = dict_representation #dictionary of lists
        return dict_representation #self.shape_archive[shape]

    def connected_graph(self, shape):
        if self.metrics.name not in ['taxicab_search_3d']: raise TypeError
        return nx.from_dict_of_lists(self.connected_dict(shape=shape)) #standard nx graph object

    def connected_component_subgraphs(self, shape, filter_func = lambda x: len(x)>1):
        if self.metrics.name not in ['taxicab_search_3d']: raise TypeError
        G = self.connected_graph(shape=shape)
        #G.remove_nodes_from(nx.isolates(G))
        return filter(filter_func, nx.connected_component_subgraphs(G)) #generator that generates filtered graphs

    def connected_component_dicts(self, shape, filter_func = lambda x: len(x)>1):
        graphs = self.connected_component_subgraphs(shape=shape, filter_func=filter_func)
        return map(lambda graph: {cube: self.cubes[cube] for cube in graph}, graphs) # returns map object made of structure such as cubes

    def connected_component_lists(self, shape, filter_func = lambda x: len(x)>1):
        graphs = self.connected_component_subgraphs(shape=shape, filter_func=filter_func)
        return map(lambda x: list(x), graphs)  # returns generator object made of lists

    def connected_component_lists_optimised(self, shape, filter_func, on_cubes=None):
        d = self.connected_dict(shape, on_cubes=on_cubes) #3.5s for unpacking from generator into graph dict
        nodes=set(chain(d.keys(),*d.values()))
        d_maps = dict(zip(nodes, range(len(nodes))))
        d_inverse_maps = dict(enumerate(nodes))
        isolated_nodes = list(map(lambda x: d_maps[x], filter(lambda y: len(y)==0, d.keys())))
        graph = igraph.Graph(edges=[(d_maps[v], d_maps[a]) for v in d.keys() for a in d[v]])
        graph.add_vertices(isolated_nodes)
        graph_tags = graph.clusters().membership
        _, values = npi.group_by(graph_tags, values=range(len(graph_tags))) #2.5 for grouping tags
        d_components = map(lambda x: list(map(lambda edge: d_inverse_maps[edge], x)), values) #2.6 for full iteration but still return generator
        return filter(filter_func, d_components)

    def save_cubes(self, path, name):
        # assuming cubes are elements of dictionary {tuple -> numpy array of point ids}
        # data is being retrieved quite slowly if we have dictionary of numpy arrays of different length; this is optimisation

        t = time(); print('...... creating pointers:', end='');
        pointers_by_cube_size = defaultdict(lambda: [])
        for n in self.cubes: pointers_by_cube_size[len(self.cubes[n])].append(n)  # cubes grouped by their sizes
        print(round(time() - t, 3))

        t = time(); print('...... creating files for cubes:');
        for pointer in tqdm(pointers_by_cube_size):  # 6.3s
            subcubecloud = {cube_key: self.cubes[cube_key] for cube_key in pointers_by_cube_size[
                pointer]}  # subdictionary cubes filtered by property that size of cube = pointer
            subcubecloud_values = list(subcubecloud.values())
            subcubecloud_keys = list(subcubecloud.keys())
            # with open(path+'/'+name+'_keys'+str(pointer) +'.pkl', 'wb') as f:
            # pickle.dump(subcubecloud_keys, f)
            np.save(path + '/' + name + '_values' + str(pointer) + '.npy', subcubecloud_values)
            np.save(path + '/' + name + '_keys' + str(pointer) + '.npy', subcubecloud_keys)

    def retrieve_cubes(self, path, capture_slices=True):
        # data is being retrieved quite slowly in case if we have dictionary of numpy arrays of different length;
        # (10secs for 20M points which is the same as performing algorithm in a straigh way);
        # this is optimisation that avoids zeroing unneccessary cells while saving;
        # capture_slices parameter is designed to capture cube ids in numpy format if we need it.
        if self.cubes is None:
            files_within_path = os.listdir(path)
            files_with_values = sorted([n for n in files_within_path if 'values' in n])
            files_with_keys = sorted([n for n in files_within_path if 'keys' in n])
            subcubeclouds = []
            if len(files_with_values) != len(files_with_keys):
                raise ValueError('keys of subcubes are inconsistent with values of subcubes')

            if capture_slices: cubeslices = []
            for i in tqdm(range(len(files_with_values))):
                subcubecloud_values = np.load(path + '/' + files_with_values[i])  # 0.2s for 27M points
                subcubecloud_keys = np.load(path + '/' + files_with_keys[i])  # 0.1s for 27M points
                subcubecloud_keys = subcubecloud_keys.tolist()  # 0.6s(tolist) for 27M points
                if capture_slices: cubeslices.append(subcubecloud_keys)
                subcubecloud_keys = list(map(lambda n: tuple(n), subcubecloud_keys))  # 0.5s for 27M points (vs 1.0 without tolist)
                # with open(path+'/'+files_with_keys[i], 'rb') as f: #1.55s (vs 1.2s via np.save) for 27M points
                # subcubecloud_keys = pickle.load(f)
                subcubeclouds.append(dict(zip(subcubecloud_keys, subcubecloud_values)))  # 0.6s for 27M points
            if capture_slices: self.cube_slices = np.array(list(chain.from_iterable(cubeslices)))  # 0.5s for 27M points
            cubecloud = dict(chain.from_iterable(subcubecloud.items() for subcubecloud in subcubeclouds))  # 0.05s for 27M points (300 dictionaries)
            self.cubes = cubecloud

#fast test:
#nx.draw(nx.from_dict_of_lists({0:[1,2], 4:[2,0], 5:[]}), with_labels=True)

class Lidar:
    def __init__(self, file):
        self.inFile = laspy.file.File(file, mode='r')
        self.header = [spec.name for spec in self.inFile.point_format]  # what kind of data are kept in points?
        # usually, ['X', 'Y', 'Z', 'intensity', 'flag_byte', 'raw_classification', 'scan_angle_rank', 'user_data', 'pt_src_id', 'gps_time']
        # print([x.name for x in in_file.header.header_format]) #this should be smth useful
        self.point_records = None
        self.points = None
        self.extract_points()


    def extract_points(self):
        t = time()
        print('getting point_records:', end=' ')
        if self.point_records == None:
            self.point_records = self.inFile.points.copy()
            self.points = self.point_records['point']
        print(len(self.points), 'points found in ', round(time() - t, 3))
        
    def extract(self):
        cubecloud = PointcloudScientist(self.points, translate_info=(0, 0, 0))
        cubecloud.find_cubes(connect_database=False)
        #cubecloud.plot3d()

lidar = Lidar('D:\lidar_test_spain\SIMULATION000003.las')
lidar.extract()