
#E = RunEngine({})
dcm = EpicsMotor('X11B1:OP:DCM:BraggTop',name='dcm')
dcme = blcg('X11B1:OP:DCM:',name='dcme') 
adc1 = adc('X11B1:EX:CHANNELFLOAT0:IN',name='adc1',read_attrs=['value'])
adc2 = adc('X11B1:EX:CHANNELFLOAT1:IN',name='adc2',read_attrs=['value'])
adc3 = adc('X11B1:EX:CHANNELFLOAT2:IN',name='adc3',read_attrs=['value'])
i0 = newadc('X11B1:EX:ADC:',name='i0',read_attrs=['ch0'])
i1 = newadc('X11B1:EX:ADC:',name='i1',read_attrs=['ch1'])
i3 = newadc('X11B1:EX:ADC:',name='i2',read_attrs=['ch2'])
#RE(scan([adc1]))
#plan1 = scan([det],motor,0,5,10)
#plot1 = LivePlot('det','motor')
