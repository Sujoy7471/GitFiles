#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int particle = 250, itr = 200;
    float h = 0.005;
    double x[particle][itr], y[particle][itr], vx[particle][itr], vy[particle][itr];
    float collrad = 0.02, dis;
    double temp_vx, temp_vy;
    float offset = 0.4857;   // This is used because for (0,0), there were some issue due to both position and velocity becoming 0

    // Initialize position and velocity for each particle in uniform distribution
    for (int p = 0; p < particle; p++) {
        x[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        y[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        vx[p][0] = 5.0*(-1 + (2.0*rand() / (double)RAND_MAX));
        vy[p][0] = 5.0*(-1 + (2.0*rand() / (double)RAND_MAX));
    }

    // Open file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Analysis loop for each time step
    for (int i = 0; i < itr - 1; i++) 
    {
        for (int p = 0; p < particle; p++) 
        {
            // Updating the position
            x[p][i+1] = x[p][i] + h * vx[p][i];
            y[p][i+1] = y[p][i] + h * vy[p][i];

            // Reflect velocity if hitting a boundary
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

            // Velocity interchange by collision
            for (int p1 = 0; p1 < particle ; p1 ++)
            {
                for (int p2 = p1 + 1; p2 < particle; p2++)
                {
                    dis = sqrt(pow(x[p1][i+1] - x[p2][i+1], 2) + pow(y[p1][i+1] - y[p2][i+1], 2));
                    if (dis < collrad)
                    {
                        temp_vx = vx[p1][i+1];
                        temp_vy = vy[p1][i+1];
                        vx[p1][i+1] = vx[p2][i+1];
                        vy[p1][i+1] = vy[p2][i+1];
                        vx[p2][i+1] = temp_vx;
                        vy[p2][i+1] = temp_vy;
                    }
                }
            }
        }

        // Write all particles' data in **one row per time step**
        for (int p = 0; p < particle; p++) {
            fprintf(file, "%lf,%lf,%lf,%lf", x[p][i+1], y[p][i+1], vx[p][i+1], vy[p][i+1]);
            if (p < particle - 1) {
                fprintf(file, ",");  // Add comma between particles
            }
        }
        fprintf(file, "\n");  // New line after all particles in a time step
    }

    fclose(file);
    return 0;
}