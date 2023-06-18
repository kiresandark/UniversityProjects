net = newp([-6 6 ; -6 6], 3);
z = [-1 1; -1 1; -1 1];
x = [-1; 0; 1];
net.IW{1,1} = z;
net.b{1} = x;
p1 = {[-6; -6] [-2; 2] [2; 3] [-2; -2] [-2 ; -2]};
a1 = sim(net, p1);

net = newlin([-6 6 ; -6 6], 3);
net.IW{1,1} = z;
net.b{1} = x;
a2 = sim(net, p1);

p2 = [0 2];
t = [0 1];  
net = newlind(p2, t);
a3 = sim(net, p2);
error = t - a3;
plot(error);

net.trainFcn = 'trainlm';
net = train(net, p2, t)
a4 = sim(net, p2);
error = t - a4;
plot(error);
