#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
    FILE *fp;
    fp = fopen("input01.txt", "r");
    
    int a = 0;
    int b = 0;
    int res = 0;
    fscanf (fp, "%d", &a);

    while (!feof (fp)) { 
      fscanf (fp, "%d", &b);

      if (a < b) {
        res++;
      }

      a = b;
    }

    printf("%d\n", res);

    fclose (fp);
    return 0;
}
