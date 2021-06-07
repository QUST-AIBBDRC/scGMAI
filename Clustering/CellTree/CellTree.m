%% load results
idx = readtable(strcat('data_celltreeoutput.txt'));
idx = table2array(idx(:,2:end));
Z = linkage(idx,'ward');
idx = cluster(Z,'maxclust',n);
csvwrite('data_celltree.csv',idx)

