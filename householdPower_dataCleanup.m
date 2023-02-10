% clc;clear;
% Run this code in the folder containing household_power_consumption.csv file.
% This file also should not be in the folder.
clc;clear
householdpowerconsumption=readtable('household_power_consumption.csv')


dt=householdpowerconsumption(:,1:2);
unixTime = posixtime(datetime(strcat(string(dt.Date),{' '},string(dt.Time))));
% TimeBase = min(unixTime);
% TimeAxis=unixTime-unixTimeMin;

activPow=householdpowerconsumption.Global_active_power;
reatPow=householdpowerconsumption.Global_reactive_power;
voltg = householdpowerconsumption.Voltage;
globIntensity = householdpowerconsumption.Global_intensity;
met1 =householdpowerconsumption.Sub_metering_1;
met2 = householdpowerconsumption.Sub_metering_2;
met3 =householdpowerconsumption.Sub_metering_3;

dataArr= [unixTime activPow reatPow voltg globIntensity met1 met2 met3];


for j=1:size(dataArr,2)
    i
    dataArr(isnan(dataArr(:,j)),:)=[];
end

data = array2table(dataArr);
data.Properties.VariableNames = householdpowerconsumption.Properties.VariableNames(2:end);
writetable(data,'CA1_cleanedData.csv');


L=size(dataArr,1);
data1= array2table(dataArr(1:L/4,:)) ;
data2= array2table(dataArr(L/4+1:L/2,:)); 
data3= array2table(dataArr(L/2+1:3*L/4,:)); 
data4= array2table(dataArr(3*L/4+1:L,:)) ;
data1.Properties.VariableNames = householdpowerconsumption.Properties.VariableNames(2:end);
data2.Properties.VariableNames = householdpowerconsumption.Properties.VariableNames(2:end);
data3.Properties.VariableNames = householdpowerconsumption.Properties.VariableNames(2:end);
data4.Properties.VariableNames = householdpowerconsumption.Properties.VariableNames(2:end);
writetable(data1,'CA1_cleanedData1.csv');
writetable(data2,'CA1_cleanedData2.csv');
writetable(data3,'CA1_cleanedData3.csv');
writetable(data4,'CA1_cleanedData4.csv');
