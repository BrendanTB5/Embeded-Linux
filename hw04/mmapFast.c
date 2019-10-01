/*
Interfcing between buttons and LEDs using mmap
Brendan Mulholland ECE 434
HW 04
9/26/19
*/

#include <sys/mman.h>
#include <signal.h>   
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h> 



#define GPIO0_START_ADDR 0x44E07000
#define GPIO0_END_ADDR   0x44E09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR   0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO2_START_ADDR 0x481AC000
#define GPIO2_END_ADDR   0x481AE000
#define GPIO2_SIZE (GPIO2_END_ADDR - GPIO2_START_ADDR)

#define GPIO3_START_ADDR 0x481AE000
#define GPIO3_END_ADDR   0x481B0000
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define GPIOSET0 0x190
#define GPIOSET1 0x194

#define output (1 << 29)  // GPIO 1


void signal_handler(int sig);

int alive = 1;
volatile void *gpio1_addr;
int fd;


void signal_handler(int sig)
{
    printf( "\nExiting\n" );
    munmap((void *)gpio1_addr, GPIO1_SIZE);
    close(fd);
   
   a
   exit(2);
}


void main(){
    
    
    signal(SIGINT, signal_handler);
    
    
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;

    fd = open("/dev/mem", O_RDWR);
    
    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    
    
    gpio1_setdataout_addr   = gpio1_addr + GPIOSET1;
    gpio1_cleardataout_addr = gpio1_addr + GPIOSET0;

    
    if(gpio1_addr == MAP_FAILED){
        printf("The mapping to RAM has failed. Exiting \n");
        exit(1);
    }
    
    printf("The memory has mapped correctly.\n");
    
    while(1){
        *gpio1_cleardataout_addr = output;
        //usleep(1);
        *gpio1_setdataout_addr = output;
        //usleep(1);
    }

    
    

}