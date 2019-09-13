// Mark Procter
// ECE434
// Homework 2

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "gpio-utils.h"

int main()
{
    toggle = 0;
    gpio_export(gpio);
	
	//SET DIRECTION
	gpio_set_dir(gpio, "out");
			
	gpio_fd = gpio_fd_open(gpio, O_RDONLY);

    while (1)
    {
        toggle = !toggle;
        gpio_set_value(gpio, toggle);
    }

    gpio_fd_close(gpio_fd);
	return 0;        
}