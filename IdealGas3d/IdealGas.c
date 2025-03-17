#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int particle = 40, itr = 50;
    float h = 0.01;
    double x[particle][itr], y[particle][itr], z[particle][itr]; 
    double vx[particle][itr], vy[particle][itr], vz[particle][itr];
    float collrad = 0.01, dis;
    double temp_vx, temp_vy, temp_vz;
    float offset = 0;   // Offset to avoid initial zero issues
    clock_t start, end;
    double runtime;

    // Initialize position and velocity for each particle in a uniform distribution
    for (int p = 0; p < particle; p++) {
        x[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        y[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        z[p][0] = (offset + (double)rand() / (double)RAND_MAX);
        
        vx[p][0] = 5.0 * (-1 + 2.0 * (double)rand() / (double)RAND_MAX);
        vy[p][0] = 5.0 * (-1 + 2.0 * (double)rand() / (double)RAND_MAX);
        vz[p][0] = sqrt(50 - (vx[p][0])*(vx[p][0]) - (vy[p][0])*(vy[p][0]));
    }


    start = clock();                    // Starting the clock

    // Open file for writing
    FILE *file = fopen("output_3d.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Simulation loop for each time step
    for (int i = 0; i < itr - 1; i++) 
    {
        for (int p = 0; p < particle; p++) 
        {
            // Updating the position
            x[p][i+1] = x[p][i] + h * vx[p][i];
            y[p][i+1] = y[p][i] + h * vy[p][i];
            z[p][i+1] = z[p][i] + h * vz[p][i];

            // Reflect velocity if hitting a boundary (for all axes)
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

            if (z[p][i+1] < 0.0 + offset || z[p][i+1] > 1.0 + offset) {
                vz[p][i+1] = -vz[p][i];
            } else {
                vz[p][i+1] = vz[p][i];
            }

            // Velocity interchange by collision
            for (int p1 = 0; p1 < particle ; p1++)
            {
                for (int p2 = p1 + 1; p2 < particle; p2++)
                {
                    dis = sqrt(pow(x[p1][i+1] - x[p2][i+1], 2) +
                               pow(y[p1][i+1] - y[p2][i+1], 2) +
                               pow(z[p1][i+1] - z[p2][i+1], 2));

                    if (dis < collrad)
                    {
                        temp_vx = vx[p1][i+1];
                        temp_vy = vy[p1][i+1];
                        temp_vz = vz[p1][i+1];

                        vx[p1][i+1] = vx[p2][i+1];
                        vy[p1][i+1] = vy[p2][i+1];
                        vz[p1][i+1] = vz[p2][i+1];

                        vx[p2][i+1] = temp_vx;
                        vy[p2][i+1] = temp_vy;
                        vz[p2][i+1] = temp_vz;
                    }
                }
            }
        }

        // Write all particles' data in **one row per time step**
        for (int p = 0; p < particle; p++) {
            fprintf(file, "%lf,%lf,%lf,%lf,%lf,%lf", 
                    x[p][i+1], y[p][i+1], z[p][i+1], vx[p][i+1], vy[p][i+1], vz[p][i+1]);
            if (p < particle - 1) {
                fprintf(file, ",");  // Add comma between particles
            }
        }
        fprintf(file, "\n");  // New line after all particles in a time step
    }
    fclose(file);

    end = clock();                                  // Noting endtime
    runtime = (double)(end - start)/CLOCKS_PER_SEC;
    printf("Runtime = %f s \n", runtime);

    // So the time relation is t = (2.6e-8)*(particle^3)*(itr)
    return 0;
}
