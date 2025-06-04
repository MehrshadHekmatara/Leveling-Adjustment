clc;
clear;
close all;

%--------------------------------------------------------------------------
%Entering question assumption data into MATLAB
data = load('data02.mat');
y = data.y;
X = data.X;
Eind = data.Eind;
Sind = data.Sind;
sigma_moshahedat = 0.1;

known_points_num = 1;
known_points_index = 1;
height_of_known_point = 100;

%obtaining number of observatios
[n, ~] = size(y);

%obtaining number of unknown points
[u, ~] = size(X);
u = u - known_points_num;

%Formation of observation vector
LO = y;

for i = 1:n
    if Sind(i) == known_points_index
        LO(i) = LO(i) + height_of_known_point;
    elseif Eind(i) == known_points_index
        LO(i) = height_of_known_point - LO(i);
    end
end

%Formation of weight vector
W = eye(n, n) * (1 / (sigma_moshahedat^2));

%Obtaining the A matrix
A = zeros(n, u);
i = 1;
while i<=n
    j = Eind(i) - 1;
    if j>=1
        A(i, j) = 1;
    end
    k = Sind(i) - 1;
    if k>=1
        A(i, k) = -1;
    end
    i = i + 1;
end
%--------------------------------------------------------------------------
%Obtaining the height of unknown points
Xcap = inv((transpose(A) * W * A)) * transpose(A) * W * LO;
%--------------------------------------------------------------------------
% LO(cap) = A * X(cap)
LOcap = A * Xcap;
%--------------------------------------------------------------------------
%Formation of the residual vector ||| V = A * Xcap - LO
V = (A * Xcap) - LO;
figure('Name' ,'residual vector')
imagesc(V)
colorbar
title('residual vector chart')
%--------------------------------------------------------------------------
%Formation of the variance-covariance matrix
Q = inv(transpose(A) * W * A);
figure('Name' ,'variance-covariance matrix')
imagesc(Q)
colorbar
title('variance-covariance matrix')
