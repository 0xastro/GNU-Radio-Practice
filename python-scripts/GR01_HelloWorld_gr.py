#Tells the shell that this file is a Python file and to use the Python interpreter to run this file. 
#Should always be included at the top to #run from the terminal. 

#!usr/bin/env Python


#Tells Python the modules to include. 
#We must always have gr to run GNU Radio applications. 
#The audio sink is included in the audio module and the signal_source_f is included in the analog module which is why we include them.

from gnuradio import gr
from gnuradio import audio
from gnuradio import analog

#Define a class called "HelloWorld_gr" which is derived from another class, gr.top_block. 
#This class is basically a container for the flow graph. 
#By deriving from gr.top_block, we get all the hooks and functions we need to add blocks and interconnect them. 

class HelloWorld_gr(gr.top_block):

#Only one member function is defined for this class: the function "init()", 
#which is the constructor of this class (The parent constructor). 

    def __init__(self):
        gr.top_block.__init__(self)

#Variable declarations for sampling rate and amplitude.

        sample_rate = 32000
        ampl = 0.1

#the documentation for analog.sig_source_f memeber function 
#static sptr gr::analog::sig_source_f::make(
#		double  	 	        sampling_freq,
#		gr::analog::gr_waveform_t  	waveform,
#		double  			wave_freq,
#		double  			ampl,
#		float  				offset = 0 
#		)
#We can see that our function analog.sig_source_f takes in 5 parameters but in our code we are only using 4. 
#There is no error because the last input offset is set to "0" by default as shown in the documentation.
#enum gr::analog::gr_waveform_t
#Types of signal generator waveforms.
#Enumerator
#GR_CONST_WAVE 	
#GR_SIN_WAVE 	
#GR_COS_WAVE 	
#GR_SQR_WAVE 	
#GR_TRI_WAVE 	
#GR_SAW_WAVE 	
 	
        src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 350, ampl)
        src1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 440, ampl)


#static sptr gr::audio::sink::make(
#	 	int  			sampling_rate,
#		const std::string  	device_name = "",
#		bool  			ok_to_block = true 
#	) 	
#Creates a sink from an audio device at a specified sample_rate. The specific audio device to use can be specified as the device_name parameter. Typical choices are: 
#    pulse
#    hw:0,0
#    plughw:0,0
#    surround51
#    /dev/dsp
#In the second input, we have a choice for what device to use for audio output. 
#If we leave it alone as "" then it'll choose the default on our machine. 

        dst = audio.sink(sample_rate, "")

#The general syntax for connecting blocks is self.connect(block1, block2, block3, ...) 
#which would connect the output of block1 with the input of block2,
#the output of block2 with the input of block3 and so on. #We can connect as many blocks as we wish with one connect() call. 

#However this only work when there is a one-to-one correspondence. 
#If we go back to our initial flowgraph, there are 2 inputs to the Audio Sink block. 
#The way to connect them is by using the syntax above. 
#The first line connects the only output of src0 (350 Hz waveform) to the first input of dst (Audio Sink).
#The second line connects the only output of src1 (440 Hz waveform) to the second input of dst (Audio Sink). 
#The code so far is equivalent to the flowgraph we have created in the beginning; 

        self.connect(src0, (dst, 0))
        self.connect(src1, (dst, 1))

#start the flowgraph and provide a keyboard interrupt. 
if __name__ == '__main__':
    try:
        HelloWorld_gr().run()
    except [[KeyboardInterrupt]]:
        pass
    
