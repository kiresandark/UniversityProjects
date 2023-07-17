package com.example;

import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import static java.lang.Math.*;

public class Solver {
    private double a, b, step, yZero;
    NumberFormat formatter = new DecimalFormat("#0.0000");
    public Solver() {
    }
    public void execute() {
    System.out.println("Метод Эйлера");
    readInput();
    solveEulerBasic(a, b, step, yZero);
    System.out.println("Усовершенствованный метод Эйлера");
    readInput();
    solveEulerAdvance(a, b, step, yZero);
    System.out.println("Метод Рунге-Кутта");
    readInput();
    solveRungeKutt(a, b, step, yZero);
    }
    private void readInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите начало отрезка xn: ");
        a = Double.parseDouble(scanner.nextLine());
        System.out.print("Введите конец отрезка xk: ");
        b = Double.parseDouble(scanner.nextLine());
        System.out.print("Введите шаг h: ");
        step = Double.parseDouble(scanner.nextLine());
        System.out.print("Введите yо: ");
        yZero = Double.parseDouble(scanner.nextLine());
    }
    private void printResults(List<Double> xValues, List<Double> yValues) {
    for(int i = 0; i < xValues.size(); i++) {
    System.out.println("X[" + i + "]=" + formatter.format(xValues.get(i)) + " Y[" + i + "]=" +
    formatter.format(yValues.get(i)));
    }
    System.out.println("\n");
    }
    private void solveEulerBasic(double a, double b, double step, double yZero) {
    int iterationCount = (int)(ceil(b-a)/step);
    List<Double> xValues = new ArrayList<>();
    List<Double> yValues = new ArrayList<>();
    double y = yZero;
    double x = a;
    xValues.add(x);
    yValues.add(y);
    double yDer, yDelta;
    for(int i = 0; i < iterationCount; i++) {
    yDer = x + cos(y/sqrt(2));
    yDelta = step*yDer;
    y += yDelta;
    x += step;
    xValues.add(x);
    yValues.add(y);
    }
    System.out.println("Результаты решения ОДУ методом Эйлера\n");
    printResults(xValues, yValues);
    }
    private void solveEulerAdvance(double a, double b, double step, double yZero) {
    int iterationCount = (int)(ceil(b-a)/step);
    List<Double> xValues = new ArrayList<>();
    List<Double> yValues = new ArrayList<>();
    double y = yZero;
    double x = a;
    double f, hy, x2, y2, f2, hy2;
    xValues.add(x);
    yValues.add(y);
    for(int i = 0; i < iterationCount; i++) {
    f = euAdvFunc(x, y);
    hy = f*step/2;
    x2=x+step/2;
    y2=y+hy;
    f2 = euAdvFunc(x2, y2);
    hy2 = step*f2;
    y += hy2;
    x += step;
    xValues.add(x);
    yValues.add(y);
    }
    System.out.println("Результаты решения ОДУ усовершенствованным методом Эйлера\n");
    printResults(xValues, yValues);
    }
    private double euAdvFunc(double x, double y) {
    return 0.145*(pow(x, 2) + cos(0.5*x))+0.842*y;
    }
    private void solveRungeKutt(double a, double b, double step, double yZero) {
    int iterationCount = (int)(ceil(b-a)/step);
    List<Double> xValues = new ArrayList<>();
    List<Double> yValues = new ArrayList<>();
    double y = yZero;
    double x = a;
    double f1, k1, f2, k2, f3, k3, f4, k4, dy;
    xValues.add(x);
    yValues.add(y);
    for(int i = 0; i < iterationCount; i++) {
    f1 = rungeKuttFunc(x, y);
    k1 = step * f1;
    f2 = rungeKuttFunc(x+step/2, y+k1/2);
    k2 = step * f2;
    f3 = rungeKuttFunc(x+step/2, y+k2/2);
    k3 = step * f3;
    f4 = rungeKuttFunc(x+step, y+k3);
    k4 = step * f4;
    dy = (k1+k2*2+k3*2+k4)/6;
    y += dy;
    x += step;
    xValues.add(x);
    yValues.add(y);
    }
    System.out.println("Результаты решения ОДУ усовершенствованным методом Эйлера \n");
    printResults(xValues, yValues);
    }
    private double rungeKuttFunc(double x, double y) {
    return 1-sin(x+y)+0.5*y/(x+2);
    }
    }
