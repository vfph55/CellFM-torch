import scanpy as sc

# 读取h5ad文件
adata_1 = sc.read_h5ad('/F00120250015/cell_datasets/xiaoqianCHENG/CellFM-torch/data/HumanPBMC.h5ad')
adata_2 = sc.read_h5ad('/F00120250015/cell_datasets/xiaoqianCHENG/CellFM-torch/data/Pancrm.h5ad')
adata_3 = sc.read_h5ad('/F00120250015/cell_datasets/xiaoqianCHENG/CellFM-torch/data/PBMC_368K.h5ad')

# 输出数据的基本信息
print(adata_1)
print(adata_1.obs.head())       # 细胞元信息前几行
# 在列名为batch的obs中统计有多少个不同的批次
print(adata_1.obs['batch'].value_counts())
print(adata_2.obs["batch"].value_counts())
print(adata_3.obs["batch"].value_counts())  

