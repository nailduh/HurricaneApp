filename = 'C:\Users\herna\Downloads\Florida Boil Notice\tl_2017_12_cousub\tl_2017_12_cousub.shp'; % Specify the path to your shapefile
S = shaperead(filename);
data = readtable('BoilNoticeList.xlsx', 'ReadVariableNames', false, 'Range', 'A3:A162');  % Adjust range as needed
Counties = data{:, 1}; 
BoilNoticeCounties = unique(Counties);

for i = 1:length(S)
    S(i).underBoilNotice = false; % Initialize with a default value
end

for i = 1:length(S)
    elementToCheck = S(i).NAME;  % 'apple'
    if ismember(elementToCheck, BoilNoticeCounties)
        S(i).underBoilNotice = true;
    end
end

% Step 3: Create a figure
figure;
hold on;

for i = 15:20
    S(i).underBoilNotice = true;
end

% Step 4: Plot the counties
for i = 1:length(S)
    % Step 5: Shade the selected counties
   if S(i).underBoilNotice == true % Assuming 'Name' is the property
        % Shade with a specific color
        fill(S(i).X, S(i).Y, 'r', 'FaceAlpha', 0.2); % Red with transparency
    else
        % Plot the other counties with a default color
        fill(S(i).X, S(i).Y, 'w', 'EdgeColor', 'k'); % White with black edges
    end
end

% Optional: Set axes properties
axis equal;
xlabel('Longitude');
ylabel('Latitude');
title('Shaded Counties');
hold off;
