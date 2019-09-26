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

#define GPIO_DATAIN 0x138
#define GPIOSET0 0x190
#define GPIOSET1 0x194

#define button1 (1 << 2)  // GPIO 2
#define button2 (1 << 29) // GPIO 1

#define USR3 (1<<24)
#define USR2 (1<<23)

void signal_handler(int sig);

int alive = 1;


void signal_handler(int sig)
{
    printf( "\nExiting\n" );
    alive = 0;
}


void main(){
    
    
    signal(SIGINT, signal_handler);
    
    volatile void *gpio1_addr;
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;
    volatile unsigned int *gpio1_datain_addr;
    
    volatile void *gpio2_addr;
    volatile unsigned int *gpio2_datain_addr;
    
    
    int fd = open("/dev/mem", O_RDWR);
    
    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    
    if(gpio1_addr == MAP_FAILED || gpio2_addr == MAP_FAILED){
        printf("The mapping to RAM has failed. 1111 Exiting \n");
        exit(1);
    }
    
    gpio2_addr = mmap(0, GPIO2_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO2_START_ADDR);
    if(gpio1_addr == MAP_FAILED || gpio2_addr == MAP_FAILED){
        printf("The mapping to RAM has failed. 2222 Exiting \n");
        exit(1);
    }
    
    gpio1_setdataout_addr   = gpio1_addr + GPIOSET1;
    gpio1_cleardataout_addr = gpio1_addr + GPIOSET0;
    gpio1_datain_addr = gpio1_addr + GPIO_DATAIN;
    
    gpio2_datain_addr = gpio2_addr + GPIO_DATAIN;
    
    
    if(gpio1_addr == MAP_FAILED || gpio2_addr == MAP_FAILED){
        printf("The mapping to RAM has failed. Exiting \n");
        exit(1);
    }
    
    printf("The memory has mapped correctly.\n");
    
    while(alive){
        if(*gpio2_datain_addr & button1){
            *gpio1_cleardataout_addr = USR2;
        }
        else{
            *gpio1_setdataout_addr = USR2;
        }
        if(*gpio1_datain_addr & button2){
            *gpio1_cleardataout_addr = USR3;
        }
        else{
            *gpio1_setdataout_addr = USR3;
        }
        
        usleep(200);
        
        
    }
    
    munmap((void *)gpio1_addr, GPIO1_SIZE);
    munmap((void *)gpio2_addr, GPIO2_SIZE);
    close(fd);
   
   
   exit(2);
    

}