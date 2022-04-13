# frameControl(self, i)
# i is an integer indicating viewer frame control 'button' to execute:    

# 	-6 go to start
# 	-5 play reverse
# 	-4 go to previous keyframe
# 	-3 step back by increment
# 	-2 go back previous keyframe or increment, whichever is closer
# 	-1 step back one frame
# 	0 stop
# 	+1 step forward one frame
# 	+2 go to next keyframe or increment, whichever is closer
# 	+3 step forward by increment
# 	+4 go to next keyframe
# 	+5 play forward
# 	+6 go to end 

# Returns: True