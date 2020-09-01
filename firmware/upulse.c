#include "zerynth.h"

// #define printf(...) vbl_printf_stdout(__VA_ARGS__)
#define printf(...)

void us_delay_poll(uint32_t us) {
    us = us * (_system_frequency / 1000000);
    uint32_t time = *vosTicks();
    while (*vosTicks() - time < us);
}



C_NATIVE(upulse){
    C_NATIVE_UNWARN();
    
    int32_t pin;
    uint32_t us;
    uint32_t n_pulse;

    if (parse_py_args("iii", nargs, args, &pin, &us, &n_pulse) != 3)
        return ERR_TYPE_EXC;
    
    void *port = vhalPinGetPort(pin);
    int pad = vhalPinGetPad(pin);
    
    // printf("us %i * n_pulse %i = %i\n",us, n_pulse, us*n_pulse);
    
    for (int16_t i=n_pulse; i>0 ;i--)
    
    {
        vhalPinFastClear(port, pad);
        us_delay_poll(us);
        vhalPinFastSet(port, pad);
        us_delay_poll(us);
    }
    
    return ERR_OK;

}