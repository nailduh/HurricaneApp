% Step 1: Import the data
% Replace 'your_file.xlsx' with the name of your Excel file
data = readtable('BoilNoticeList.xlsx', 'ReadVariableNames', false, 'Range', 'A3:A162');  % Adjust range as needed
Counties = data{:, 1}; 
BoilNoticeCounties = unique(Counties);
