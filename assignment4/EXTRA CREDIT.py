from earsketch import *

init()# This function can optionally be called at the start of the script (in previous versions of EarSketch this was required).
setTempo(120)# Sets the Project's Tempo to 110 Beats Per Minute

beatPattern1 = "00000---0---0---"*2
makeBeat(HIPHOP_FUNKBEAT_001, 1, 2.0, beatPattern1)
beatPattern2 = "000000000---0---"*2
makeBeat(HIPHOP_FUNKBEAT_001, 1, 4.0, beatPattern2)

fitMedia(HIPHOP_FUNKBEAT_001, 2, 1, 6) #Adds an audio file to a specified track at specified start and end times. The audio file will be repeated or cut short as needed to fill the specified amount of time.


finish() # This function can optionally be called at the end of the script (in previous versions of EarSketch this was required).