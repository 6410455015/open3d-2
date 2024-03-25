import open3d as o3d
import numpy as np

# kota = "kota_circuit2.ply"
# pcd = o3d.io.read_point_cloud(kota)
# o3d.visualization.draw_geometries_with_editing([pcd])
crop = "cropped_1.ply"
pcd1 = o3d.io.read_point_cloud("crop")
o3d.visualization.draw_geometries([pcd1])

# pcd1.estimate_normals(
#     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.4, max_nn=100))
# o3d.visualization.draw_geometries([pcd1])



# normals1 = np.asarray(pcd1.normals)
# colors1 = np.asarray(pcd1.colors)

# for i in range(len(normals1)):
# 	if(normals1[i][2]>= 0.95):
# 		colors1[i][0] = 1
# 		colors1[i][1] = 0
# 		colors1[i][2] = 0
	
# pcd1.colors = o3d.utility.Vector3dVector(colors1)
# o3d.visualization.draw_geometries([pcd1])