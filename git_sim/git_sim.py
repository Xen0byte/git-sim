from manim import *
import git, sys, numpy

from git_sim_reset import *
from git_sim_revert import *
from git_sim_branch import *
from git_sim_tag import *

class GitSim(MovingCameraScene):
    def __init__(self, args):
        super().__init__()
        self.args = args

        if ( self.args.light_mode ):
            self.fontColor = BLACK
        else:
            self.fontColor = WHITE

    def construct(self):
        if self.args.subcommand == 'branch':
            self.command = GitSimBranch(self)
        elif self.args.subcommand == 'tag':
            self.command = GitSimTag(self)
        elif self.args.subcommand == 'reset':
            self.command = GitSimReset(self)
        elif self.args.subcommand == 'revert':
            self.command = GitSimRevert(self)

        self.command.execute()