% Run this code from the folder containing the folder ghg_data 
% that ONLY contains the files ghg.gid.siteXXXX.dat.
clc;clear
listing=dir('ghg_data');
for i=3:size(listing)
    i
    d=importdata(strcat('ghg_data/',listing(i).name));
    dataArr(:,i-2)=d(:);
end

dataArr=dataArr';
dataArr1=dataArr(1:1500,:);
dataArr2=dataArr(1501:end,:);

data1 = array2table(dataArr1);
data2 = array2table(dataArr2);
data1.Properties.VariableNames = string(0:size(dataArr1,2)-1);
data2.Properties.VariableNames = string(0:size(dataArr2,2)-1);

writetable(data1,'CA1_1c_greenhouse_cleanedData_part1.csv');
writetable(data2,'CA1_1c_greenhouse_cleanedData_part2.csv');
