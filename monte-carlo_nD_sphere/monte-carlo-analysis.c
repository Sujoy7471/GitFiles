#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Define a struct to return two values
typedef struct {
    int count;
    int itr;
} MonteCarloResult;

MonteCarloResult montecarlo(int N, float R)
{                                   
    MonteCarloResult result;
    result.itr = (int)pow(10, N);  // Number of iterations
    result.count = 0;              // Count of points inside the hypersphere
    
    for (int i = 0; i < result.itr; i++)
    {
        double rad_v = 0.0;         // Radius vector parameter 
        for (int j = 0; j < N; j++)
        {
            double x = ((double)rand() / RAND_MAX) * 2 * R - R;  // Generate random points
            rad_v += x * x;          // Update radius vector
        }
        if (rad_v <= R * R)
        {
            result.count++;          // Update count
        }
    }

    return result;  // Return struct with both values
}

int main()
{
    MonteCarloResult result = montecarlo(2, 1);  // Call function

    float m = result.count / (float)result.itr;  // Compute ratio
    printf("%f\n", m);  // Print result

    return 0;
}
