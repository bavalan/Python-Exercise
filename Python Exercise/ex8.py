class LightSwitch():
    ''' Class representing a light switch '''

    def __init__(self, position):
        '''(Switch, str) -> NoneType

        Create a switch that is either On or Off

        REQ: position = "on" or "off"
        '''

        # The position of the switch
        if(position == "on"):
            self.Switch = True
        else:
            self.Switch = False

    def __str__(self):
        '''(Switch) -> str
        Return a string representing the switches position
        '''
        b = True
        # If the Switch is on
        if (self.Switch == b):
            ReturnPosition = ("I am on")
        # If the switch is off
        else:
            ReturnPosition = ("I am off")

        return ReturnPosition

    def turn_on(self):
        '''(Switch) -> NoneType
        Turn the switch on
        '''
        # If the switch is on
        self.Switch = True

    def turn_off(self):
        '''(Switch) -> NoneType
        Turn the switch off
        '''
        # If the switch is off
        self.Switch = False

    def flip(self):
        '''(Switch) -> NoneType
        Turn the switch off turn it on, if the switch if on turn it off
        '''

        # If the switch if on turn it off
        self.Switch = not(self.Switch)


class SwitchBoard():
    ''' Class representing a switch board '''

    def __init__(self, A):
        '''(Board, int) -> NoneType

        Create a switch board contaning several of switches

        REQ: A > 0
        '''
        # An empty list containing several switches
        self.Board = []
        # For switch in the switchboard
        for x in range(A):
            # Turn switches off
            self.Board.append(LightSwitch("off"))

    def __str__(self):
        '''(Board) -> str
        Return a string representing the switches that are on
        '''

        b = True

        # Message saying which switches are on
        On = ("The following switches are on: ")
        # For every switch in the switch board
        for z in range(len(self.Board)):
            # If the switch is ON
            if(self.Board[z].Switch == b):
                # List all the switches that are ON with a space
                On += (str(z) + " ")
        # Return All the switches that are ON
        return On

    def flip(self, n):
        '''(Board, int) -> NoneType

        Switch the nth switch in the SwitchBoard

        REQ: n >= 0
        '''
        # If the switch isn't in the list flip n
        if ((len(self.Board) > n) and (n >= 0)):
            # Flip the nth switch
            self.Board[n].flip()

    def which_switch(self):
        '''(Board) -> list of int

        Switch the nth switch in the SwitchBoard
        '''

        b = True

        # Empty list of flipped switches
        Flips = []
        # For every switch in the switch board
        for z in range(len(self.Board)):
            # If the switch is on
            if(self.Board[z].Switch == b):
                # Added the flipped switch into the list
                Flips.append(z)
        return Flips

    def flip_every(self, n):
        # For every number from 0 to the last switch, will be flipped
        # Every nth time
        for z in range(0, len(self.Board), n):
            # Will be flipped
            self.flip(z)

    def reset(self):
        # For every switch in the Board
        for z in range(len(self.Board)):
            # Will turn off by calling the turn_off function
            self.Board[z].turn_off()

# Global Code
if __name__ == ('__main__'):

    # There are 1024 switch boards
    switchboard = SwitchBoard(1024)
    # For everynumber upuntil 1024
    for NthNumber in range(1024):
        # Flip it at every NthNumber
        switchboard.flip_every(NthNumber+1)
    print(switchboard)
