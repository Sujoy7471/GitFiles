#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Defining the initial parameters and variables
    int particle = 300, itr = 750;
    float h = 0.005;
    double x[particle][itr], y[particle][itr], vx[particle][itr], vy[particle][itr];
    float collrad = 0.01, dis;
    double temp_vx, temp_vy;
    float offset = 0;

    // Defining the initial positions and velocities of the paritcles
    for (int p = 0; p < particle; p++) {
        x[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        y[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        vx[p][0] = 5.0 * (-1 + (2.0 * rand() / (double)RAND_MAX));
        vy[p][0] = (vx[p][0] / fabs(vx[p][0]))* sqrt(25 - vx[p][0]*vx[p][0]);
    }

    // Opening a file to store data
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < itr - 1; i++) {
        // Collision with the wall
        for (int p = 0; p < particle; p++) {
            x[p][i+1] = x[p][i] + h * vx[p][i];
            y[p][i+1] = y[p][i] + h * vy[p][i];

            if (x[p][i+1] < 0.0 + offset || x[p][i+1] > 1.0 + offset) {
                vx[p][i+1] = -vx[p][i];
            } else {
                vx[p][i+1] = vx[p][i];
            }

            if (y[p][i+1] < 0.0 + offset || y[p][i+1] > 1.0 + offset) {
                vy[p][i+1] = -vy[p][i];
            } else {
                vy[p][i+1] = vy[p][i];
            }
        }

        // Collision with each other
        for (int p1 = 0; p1 < particle; p1++) {
            for (int p2 = p1 + 1; p2 < particle; p2++) {
                dis = sqrt(pow(x[p1][i+1] - x[p2][i+1], 2) + pow(y[p1][i+1] - y[p2][i+1], 2));
                if (dis < collrad) {
                    double disx = x[p2][i+1] - x[p1][i+1];
                    double disy = y[p2][i+1] - y[p1][i+1];
                    double dist = sqrt(disx * disx + disy * disy);

                    if (dist == 0) continue;

                    double nx = disx / dist;
                    double ny = disy / dist;
                    double v1n = vx[p1][i+1] * nx + vy[p1][i+1] * ny;
                    double v2n = vx[p2][i+1] * nx + vy[p2][i+1] * ny;
                    double v1t = -vx[p1][i+1] * ny + vy[p1][i+1] * nx;
                    double v2t = -vx[p2][i+1] * ny + vy[p2][i+1] * nx;

                    double temp = v1n;
                    v1n = v2n;
                    v2n = temp;

                    vx[p1][i+1] = v1n * nx - v1t * ny;
                    vy[p1][i+1] = v1n * ny + v1t * nx;
                    vx[p2][i+1] = v2n * nx - v2t * ny;
                    vy[p2][i+1] = v2n * ny + v2t * nx;
                }
            }
        }

        for (int p = 0; p < particle; p++) {
            fprintf(file, "%lf,%lf,%lf,%lf", x[p][i+1], y[p][i+1], vx[p][i+1], vy[p][i+1]);
            if (p < particle - 1) {
                fprintf(file, ",");
            }
        }
        fprintf(file, "\n");
    }

    fclose(file);
    return 0;
}
