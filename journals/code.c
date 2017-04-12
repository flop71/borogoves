#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <sys/time.h>

double lognormal_service(void);
double pareto_arrival(void);

double normal_service(void);
double normal_arrival(void);

double real_arrival(void);
double real_service(void);

double exp_arrival(void);
double exp_service(void);

int main(void) {
	int len, arrivals;
	double next_arrival, next_departure, now;

	len = 0;
	now = 0;
	next_arrival = now + pareto_arrival();
	arrivals = 1;
	next_departure = -1;

	printf("time\tlen\n");
	
	/* Simulates 1000 outage event arrivals */

	while (arrivals < 1000) { 
		if (next_departure < 0 || next_arrival < next_departure) {
			arrivals++;
			len++;
			now = next_arrival;
			next_departure = now + lognormal_service();
			next_arrival = now + pareto_arrival();
		} else {
			len--;
			now = next_departure;
			if (len > 0) {
				next_departure = now + lognormal_service();
			} else {
				next_departure = -1;
			}
		}
		printf("%f\t%d\n", now, len);
	}

	return 0;
}

double pareto_arrival(void) {
	float a;
	float b;
	float inv_fun_denom;
	float par_arr;

	a =  4; // dummy shape parameter
	b = 9000; // dummy scale parameter

	inv_fun_denom = pow(1-(rand() / (RAND_MAX + 1.0)), 1/a);
	par_arr = (b/inv_fun_denom)-b;

	return par_arr;
}


double lognormal_service (void) {
	float m;	//Mean parameter
	float s;	//stdev parameter
	float x1, x2, w, y1;
	static float y2;
	static int use_last = 0;
	float normal_result;
	float lnormal_result;


	// dummy mean log and sd log
	m =  4;
	s =  1.1;

	if (use_last) {  /* use value from previous call */
		y1 = y2;
		use_last = 0;
	} else {
		do {
			x1 = 2.0 * (rand() / (RAND_MAX + 1.0)) - 1.0;
			x2 = 2.0 * (rand() / (RAND_MAX + 1.0)) - 1.0;
			w = x1 * x1 + x2 * x2;
		} while ( w >= 1.0 );


		w = sqrt( (-2.0 * log( w ) ) / w );
		y1 = x1 * w;
		y2 = x2 * w;
		use_last = 1;
	}

	normal_result = (m + y1 * s); // produces normal distribution output
	lnormal_result = exp(normal_result);

	return lnormal_result;
}
