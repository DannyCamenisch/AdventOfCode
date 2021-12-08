#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp;
    fp = fopen("input03.txt", "r");

    // Part 1

    int arr[12] = {0};
    int gamma = 0, epsilon = 0;
    char c[13];
    char input[12*1000];
    int i, j = 0;

    while (!feof(fp)) {
        int i = 0;

        if (fscanf(fp, "%12c\n", c) != 1) {
            break;
        }

        while (i < 12) {
            arr[i] += (c[i] == '1' ? 1 : -1);
            input[j*12 + i] = c[i];
            i++;
        }

        j++;
    }

    for(i = 11, j = 0; i >= 0; i--, j++) {
        gamma |= (arr[j] > 0 ? 1 : 0) << i;
        epsilon |= (arr[j] > 0 ? 0 : 1) << i;
    }

    printf("%d\n", gamma * epsilon);

    // Part 2


    return 0;
}
