String[] linesd;
String[] linese;
String[] linesl;
int cols, rows;
int x = 70;
int y = 11;

void settings() {
  size(1300, 700);
}

void setup() {
  size(1300, 700);
  background(255);
  linesd = loadStrings("../data.txt");
  rows = linesd.length;
  String [] line = split(linesd[0], ",");
  cols = line.length;
  String[] args = {"LinearRegression"};
  linesl = loadStrings("../lr.txt");
  SecondApplet sa = new SecondApplet();
  PApplet.runSketch(args, sa);
}

public class SecondApplet extends PApplet {

  public void settings() {
    size(600, 600);
  }
  public void draw() {
    background(50);
    translate(0, height);

    scale(1, -1);
    try {
      if (linesl.length > 1) {
        String xs = linesl[0];
        String ys = linesl[1];

        String [] xss = split(xs, ",");
        String [] yss = split(ys, ",");

        float mayx = float(xss[xss.length - 2]);
        float menx = float(xss[0]);
        float mayy = float(yss[0]);
        float meny = float(yss[0]);

        for (int i = 0; i < yss.length; i++) {
          if (float(yss[i]) > mayy) mayy = float(yss[i]);
          if (float(yss[i]) < meny) meny = float(yss[i]);
        }

        float []x = new float[xss.length - 1];
        float []y = new float[yss.length - 1];
        fill(50);

        //rect(cx - 10, cy - 10, clon + 10, calt + 10);
        float xsum = 0;
        float ysum = 0;

        for (int i = 0; i < x.length; i++) {
          //x[i] = map(float(xss[i]), mayx, menx, 0, 200);
          x[i] = map(float(xss[i]), menx, mayx, 0, 600);
          //y[i] = map(float(yss[i]), mayy, meny, 0, 200);
          y[i] = map(float(yss[i]), meny, mayy, 0, 600);
          xsum += x[i];
          ysum += y[i];
          noStroke();
          fill(255);
          ellipse(x[i], y[i], 7, 7);
          //println(x[i]);
        }

        float xmean = xsum/x.length;
        float ymean = ysum/y.length;

        float num = 0;
        float den = 0;

        for (int i = 0; i < x.length; i++) {
          num = num + ((x[i] - xmean) * (y[i] - ymean));
          den = den + ((x[i] - xmean) * (x[i] - xmean));
        }

        float m = num/den;

        float b = ymean - (m*xmean);

        //println(m + " " + b);

        stroke(255,0,0);
        line(0, b, width, m*width + b);
      }
    }
    catch(Exception e) {
    }
  }
}

void draw() {
  background(255);
  try {
    int ind = int(loadStrings("../index.txt")[0]);
    linesl = loadStrings("../lr.txt");
    println(ind);
    linesd = loadStrings("../data.txt");
    linese = loadStrings("../est.txt");

    String [] lined;
    String [] linee;
    for (int i = 0; i < linesd.length; i++) {
      lined = split(linesd[i], ",");
      linee = split(linese[i], ",");
      for (int j = 0; j < lined.length - 1; j++) {
        fill(255);
        if (linee[j].equals("True")) fill(0, 200, 0);
        else fill(200, 0, 0);
        rect(j*x, i*y, x, y);
        textSize(9);
        fill(0);
        float ac = float(lined[j]);
        text(ac, (j*x), (i*y) + y - 3);
      }
    }

    int xp1 = (cols - 1) * x + 20;
    int yp1 = ind * y - (y / 2);
    ellipse(xp1, yp1, 10, 10);
  }
  catch(Exception e) {
    background(255);
    println(e);
  }
}
