#!/usr/bin/env python3


#*
#*  Copyright 2015-2019 Felix Garcia Carballeira, Alejandro Calderon Mateos, Javier Prieto Cepeda, Saul Alonso Monsalve
#*
#*  This file is part of WepSIM.
#*
#*  WepSIM is free software: you can redistribute it and/or modify
#*  it under the terms of the GNU Lesser General Public License as published by
#*  the Free Software Foundation, either version 3 of the License, or
#*  (at your option) any later version.
#*
#*  WepSIM is distributed in the hope that it will be useful,
#*  but WITHOUT ANY WARRANTY; without even the implied warranty of
#*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#*  GNU Lesser General Public License for more details.
#*
#*  You should have received a copy of the GNU Lesser General Public License
#*  along with WepSIM.  If not, see <http://www.gnu.org/licenses/>.
#*


#
# Import
#
import sys
import os
from googletrans import Translator


#
#
#
i18n_eltos = {} ;

i18n_eltos['cfg'] = {

	             "General": "General",
                      "Idiom for help, examples, etc.": 		             "Idiom for help, examples, etc.",
                      "Notification speed: time before disapear": 	             "Notification speed: time before disapear",
	             "Editor": "Editor",
                      "Editor theme: light or dark": 		                     "Editor theme: light or dark",
                      "Light": 		                     			     "Light",
                      "Dark": 		                     		             "Dark",
                      "Editor mode: vim, emacs, etc.": 		                     "Editor mode: vim, emacs, etc.",
	             "Execution": "Execution",
                      "Running speed: execution speed": 		             "Running speed: execution speed",
                      "Slow": 		                     			     "Slow",
                      "Normal": 		                     		     "Normal",
                      "Fast": 		                     		             "Fast",
                      "Step-by-step: element in run mode": 		             "Step-by-step: element in run mode",
                      "Instructions": 		                     		     "Instructions",
                      "Instruction": 		                     		     "Instruction",
                      "&#181;instructions": 		                   	     "&#181;instructions",
                      "microInstruction": 		                   	     "&#181;Instruction",
                      "Breakpoint icon: icon to be used for breakpoints":            "Breakpoint icon: icon to be used for breakpoints",
                      "Limit instructions: number of instructions to be executed":   "Limit instructions: number of instructions to be executed",
                      "Limit instruction ticks: to limit clock ticks": 	             "Limit instruction ticks: clock ticks limit per instruction",
	             "Register file": "Register file",
                      "Display format": 		                     	     "Display format",
                      "Register file names": 		                             "Register file names",
                      "Numbers": 		                                     "Numbers",
                      "Labels": 		                                     "Labels",
                      "Editable registers: edit register file values": 	             "Editable registers: edit register file values",
	             "Circuitry simulation": "Circuitry simulation",
                      "Data-path color": 					     "Data-path color",
                      "Signal color": 		                                     "Signal color",
                      "Show by value or by activation": 		             "Show by value or by activation",
                      "Value": 		                     		             "Value",
                      "Activation": 		                     		     "Activation",
                      "Interactive mode: signal value can be updated": 		     "Interactive mode: signal value can be updated",
                      "Quick interactive mode: quick update of signal value":	     "Quick interactive mode: quick update of signal value",
                      "WepSIM User Interface skin": 		                     "WepSIM User Interface skin",
                      "(example)": 					             "(example)",
	             "Accesibility": "Accesibility",
                      "Active voice: external voice control": 	                     "Active voice: external voice control",
                      "Verbalization: textual or mathematical":      		     "Verbalization: textual or mathematical",
                      "WepSIM User Interface views":      	     		     "WepSIM User Interface views"

    } ;


i18n_eltos['dialogs'] = {

                        "Show Notifications":                           "Show Notifications",
                        "Show/Hide RecordBar":                          "Show/Hide RecordBar",
                        "Show/Hide ActionBar":                          "Show/Hide ActionBar",
                        "Show/Hide Slider":                             "Show/Hide Slider",
                        "Initial intro":                                "Initial intro",
                        "About WepSIM":                                 "About WepSIM",

                        "Title":                                 	"Title",
                        "Message":                                 	"Message",
                        "Duration":                                 	"Duration",

			"Confirm remove record...":     		"Do you want to remove the actual record?",
			"Close or Reset...":    			"Please click on Close to keep it, <br>or click on the Reset button to remove it.",
                        "Sure Control Memory...":			"Do you want me to save the current Control Memory contents rather than the editor contents?.",

                        "Show/Hide labels":                             "Show/Hide labels",
                        "Show/Hide content":                            "Show/Hide content",
                        "Show/Hide assembly":                           "Show/Hide assembly",
                        "Show/Hide pseudo-instructions":                "Show/Hide pseudo-instructions",

                        "Close": 		                	"Close"
    } ;


i18n_eltos['examples'] = {

             "addv + seqv.":						"addv + seqv.",
             "Alloc.s":							"Alloc.s",
             "Dummy instruction":					"Dummy instruction",
             "Exception":						"Exception",
             "Instructions":						"Instructions",
             "Interruptions":						"Interruptions",
             "Int. + syscall + except.":				"Int. + syscall + except.",
             "I/O":							"I/O",
             "Looping":							"Looping",
             "madd, mmul, mxch":					"madd, mmul, mxch",
             "Masks & shift":						"Masks & shift",
             "Matrix":							"Matrix",
             "Memory access":						"Memory access",
             "SC 1, 4-5, 8, 11-12":					"SC 1, 4-5, 8, 11-12",
             "strlen_2 + skipasciicode_2":				"strlen_2 + skipasciicode_2",
             "Subrutine":						"Subrutine",
             "syscall 1, 4-5, 8, 11-12":				"syscall 1, 4-5, 8, 11-12",
             "System call":						"System call",
             "Threads":							"Threads",
             "Vector":							"Vector",
	     "Compiler Explorer":					"Compiler Explorer",

             "example_04_01":				"Advanced example with interruption, system call, and exception.",
             "example_05_01":				"Application-specific extension: addv + seqv.",
             "example_05_03":				"Application-specific extension: madd + mmul + mxch.",
             "example_05_02":				"Application-specific extension: strlen_2 + skipasciicode_2.",
             "example_03_01":				"<b>Instructive</b> example with floating point exception.",
             "example_03_02":				"<b>Instructive</b> example with interruptions support: fetch, RETI, and .ktext/.kdata.",
             "example_03_03":				"<b>Instructive</b> example with system call support.",
             "example_04_04":				"Example of malloc + free.",
             "example_04_02":				"Example of syscall for printing/reading integer and string.",
             "example_04_03":				"Example of threads.",
             "example_03_01b":				"Example with floating point exception.",
             "example_03_02b":				"Example with interruptions support: fetch, RETI, and .ktext/.kdata.",
             "example_02_01":				"Example with programmed I/O access, and basic .text/.data segment.",
             "example_03_03b": 				"Example with system call support.",
             "example_02_02":				"Extended example with more instructions and I/O (keyboard, display).",
             "example_02_04":				"Extended example with subrutine and matrix.",
             "example_02_03":				"More extended example with masks, shift, and basic .text/.data segment.",
             "example_01_01":				"Simple example with fetch, arithmetic instructions, and basic .text segment.",
             "example_01_04":				"Simple example with fetch, branch, and basic .text/.data segment.",
             "example_01_03":				"Simple example with fetch, branch, and basic .text segment.",
             "example_01_02":				"Simple example with fetch, memory access, and basic .text/.data segment.",
             "example_06_01":				"Test example.",
	     "example_06_02":	                    	"Simple Compiler Explorer example.",

             "Advanced":				"Advanced",
             "Initial":					"Initial",
             "Intermediate":				"Intermediate",
             "Laboratory":				"Laboratory",
             "Operating Systems":			"Operating Systems",
             "Special":					"Special",

             "Load Assembly only": 			"Load Assembly only",
             "Load Firmware only": 			"Load Firmware only",
             "Copy reference to clipboard": 		"Copy reference to clipboard",
             "Share":					"Share (Android)",
	     "No examples available...": 		"No examples are available for the selected hardware",
             "Simple example":				"Simple example."

    } ;


i18n_eltos['gui'] = {

			"Loading WepSIM...":  			        "Loading WepSIM...",
			"Configuration":  			        "Configuration",
			"MicroCode":  			        	"MicroCode",
			"Assembly": 		     			"Assembly",
			"Simulator": 		     			"Simulator",
			"Examples":  			                "Examples",
			"Load":  			        	"Load",
			"Save":  			        	"Save",
                        "Restore":                                      "Restore",
			"Help":  			                "Help",
			"Help Index":  			                "Help Index",
			"Processor":  			                "Processor",
			"Assembly Debugger":  			        "Assembly Debugger",
			"Reset":  			                "Reset",
			"microInstruction": 				"&#181;Instruction",
			"Instruction":  			        "Instruction",
			"Run":  			                "Run",
			"Hardware Summary":  			        "Hardware Summary",
			"processor":  			                "processor",
			"details":  			                "details",
			"microcode":  			                "microcode",
                        "Signals": 		                     	"Signals",
                        "Behaviors": 		                     	"Behaviors",
                        "States": 	                     	        "States",
                        "Control States": 	                     	"Control States",
                        "Dependencies": 		                "Dependencies",
                        "Close": 		                	"Close",
                        "Description": 		                	"Description",
                        "Show": 		                	"Show",
                        "Show Main Memory": 		               	"Show Main Memory",
			"compile":  			                "compile",
			"Compile":  			                "Compile",
			"Please write the file name": 		        "Please write the file name",
	                "Load from this File":                          "Load from this File",

	                "labels":                                       "labels",
	                "addr":                                         "addr",
	                "ess":                                          "ess",
	                "content":                                      "content",
	                "assembly":                                     "assembly",
	                "instructions":                                 "instructions",

                        "simulator intro 1": 		                "First, you are going to load and microcompile the microcode that defines the instruction set to be used.<br>" +
									"You can use an example, load it from a file or you can edit a new one.",
                        "simulator intro 2": 		                "Next, you need to load and compile the assembly code to be executed.<br>" +
									"You can use an example, load it from a file or you can edit a new one.",
                        "simulator intro 3": 		                "Finally, in the simulator you are able to execute the microcode plus assembly loaded before. " +
									"It can be executed step by step at microinstruction level or assembly instruction level.",
                        "Prev.": 		                	"Prev.",
                        "Next": 		                	"Next",
                        "End": 		                		"End",
                        "Disable tutorial mode": 		        "Disable tutorial mode",

                        "Comment":					"Comment",
                        "Pause":					"Pause",
                        "Play":						"Play",
                        "Stop":						"Stop",
                        "Record":					"Record",

			"Registers":					"Registers",
			"Control Memory":				"Control Memory",
			"Stats":					"Stats",
			"Memory":					"Memory",
			"Keyboard+Display":				"Keyboard+Display",
			"I/O Stats":					"I/O Stats",
			"I/O Configuration":				"I/O Configuration",

                        "Recent":                                       "Recent",
			"Refresh":  			                "Refresh",
			"Welcome":  			                "Welcome"
} ;


i18n_eltos['help'] = {

	"Welcome tutorial":		"Welcome tutorial",
	"help_01_01":			"Open the welcome tutorial",

	"Simple usage tutorial":	"Simple usage tutorial",
	"help_01_02":			"Open the simple usage tutorial, for microprogramming and assembly programming",

	"Simulator: firmware":		"Simulator: firmware",
	"help_02_01":			"How to work with the firmware to be loaded into the control memory",

	"Microcode format":		"Microcode format",
	"help_02_02":			"Syntax of the microcode used",

	"Simulator: assembly":		"Simulator: assembly",
	"help_02_03":			"How to work with the assembly that use the aforementioned firmware",

	"Assembly format":		"Assembly format",
	"help_02_04":			"Syntax of the assembly elements",

	"Simulator: execution":		"Simulator: execution",
	"help_02_05":			"How the simulator can execute the assembly and firmware",

	"Simulated architecture":	"Simulated architecture",
	"help_03_01":			"Description of the simulated processor architecture",

	"Simulated signals":		"Simulated signals",
	"help_03_02":			"Main signals summary of the simulated elemental processor",

	"Hardware summary":		"Hardware summary",
	"help_03_03":			"Reference card for the simulated elemental processor hardware",

	"License, platforms, etc.":	"License, platforms, etc.",
	"help_04_01":			"WepSIM license, supported platforms, technologies used",

	"Authors":			"Authors",
	"help_04_02":			"Authors of WepSIM"

    } ;


i18n_eltos['states'] = {

			"States":  			                "States",
			"Current":  			                "Current",
			"Current State":  			        "Current State",
			"History":  			                "History",
			"None":  			                "None",
			"Empty history":  			        "Empty history",
			"Empty (only modified values are shown)":       "Empty (only modified values are shown)",
			"Differences":  			        "Differences",
			"differences with clipboard state":  	        "differences with clipboard state",
			"Meets the specified requirements": 	        "Meets the specified requirements",

                        "history": 		                	"history",
                        "Add": 		                	        "Add",
                        "'Current State' to History": 		        "'Current State' to History",
                        "Check": 		                	"Check",
                        "Copy": 		                	"Copy",
                        "to clipboard": 		                "to clipboard",

                        "Checkpoint":                                   "Checkpoint",
                        "File name":                                    "File name",
                        "Tag for checkpoint":                           "Tag for checkpoint",
                        "File to be loaded":                            "File to be loaded",
	                "Save to File":                                 "Save to File",
	                "State(s) to checkpoint":                       "State(s) to checkpoint",
	                "Record to checkpoint":                         "Record to checkpoint"

    } ;


i18n_eltos['tour_intro'] = {

			"step1":  "WepSIM helps to better understand how a computer works: " +
                                  "it is visual, interactive, integrates from signals up to interruptions, system calls, exceptions, etc. <br> " +
                                  "<br>" +
                                  "We really believe WepSIM is a revolutionary teaching tool. " +
                                  "This brief tour introduces the key elements of its interface.",

                        "step2":  "This button on the top-right let users choose the 'execution mode'.<br>" +
                                  "<br>" +
                                  "For example, the hardware to work with (e.g. the elemental processor or EP).<br>" +
                                  "Or the tutorial mode, recommended at the beginning ;-).",

                        "step3":  "On the top-right, the 'help' button opens the associated dialog.<br>" +
                                  "<br>" +
                                  "The help dialog summarizes the tutorials, descriptions, information, etc.",

                        "step4":  "And on the left, the 'examples' button open the example dialog.<br>" +
                                  "<br>" +
                                  "There are many examples that can be used to learn incrementally.",

                        "step5":  "On the top-left, the 'configuration' button opens the configuration dialog.<br>" +
                                  "<br>" +
                                  "It let users to adapt several aspects of the execution, user interface, preferences, etc.",

                        "step6":  "Congrat! You know the key elements in the WepSIM interface.<br>" +
                                  "From the 'Help' dialog you can access the 'Welcome tutorial' to continue learning.<br>"

    } ;


i18n_eltos['tutorial_simpleusage'] = {

                 "title_0":     "Simple WepSIM experience: microprogramming and programming",
                 "message_0":   "<center><img alt='wepsim screenshot' src='images/simulator/simulator011.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "This brief tutorial is going to show you how to:" +
                                "<ol>" +
                                "<li><a href='#' onclick='sim_tutorial_goframe(\"simpleusage\",0,1);'>Edit your microcode.</a></li>" +
                                "<li><a href='#' onclick='sim_tutorial_goframe(\"simpleusage\",0,3);'>Edit your assembly (based on the previous microcode).</a></li>" +
                                "<li><a href='#' onclick='sim_tutorial_goframe(\"simpleusage\",0,5);'>Execute the assembly+microcode in the simulation.</a></li>" +
                                "</ol>" +
                                "</h5>",

                 "title_1":     "Simple WepSIM experience: microprogramming and programming",
                 "message_1":   "<center><img alt='wepsim screenshot' src='images/simulator/firmware001.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "The first step is to microprogramming the firmware to be used. " +
                                "Please use the 'Microcode' button to switch to the microcode screen." +
                                "</h5>",

                 "title_2":     "Simple WepSIM experience: microprogramming and programming",
                 "message_2":   "<center><img alt='wepsim screenshot' src='images/simulator/firmware002.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "The microprogramming screen provides:" +
                                "<ul>" +
                                "<li>The editor for the microcode.</li>" +
                                "<li>The microcompiler.</li>" +
                                "<li>The hardware summary and help.</li>" +
                                "</ul>" +
                                "Once your code is ready (compiled without errors), next step is to go to the assembly screen." +
                                "</h5>",

                 "title_3":     "Simple WepSIM experience: microprogramming and programming",
                 "message_3":   "<center><img alt='wepsim screenshot' src='images/simulator/assembly002b.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "The second step is to programming the assembly to be executed. " +
                                "Please use the 'Assembly' button from both, the simulator screen or the microcode screen." +
                                "</h5>",

                 "title_4":     "Simple WepSIM experience: microprogramming and programming",
                 "message_4":   "<center><img alt='wepsim screenshot' src='images/simulator/assembly003.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "The programming screen provides:" +
                                "<ul>" +
                                "<li>The editor for the assembly code.</li>" +
                                "<li>The assembly compiler.</li>" +
                                "<li>The memory map viewer and help.</li>" +
                                "</ul>" +
                                "Once your assebly code is ready (edited and compiled without errors) next step is to go into the simulation screen." +
                                "</h5>",

                 "title_5":     "Simple WepSIM experience: microprogramming and programming",
                 "message_5":   "<center><img alt='wepsim screenshot' src='images/simulator/simulator010.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                "<p>" +
                                "<h5>" +
                                "The third step is to execute the assembly code in the simulator.<br> " +
                                "The simulator screen provides:" +
                                "<ul>" +
                                "<li>The assembly and hardware view.</li>" +
                                "<li>The detail view of registers, control memory, main memory, etc.</li>" +
                                "<li>The reset, step by step or run until breakpoint/end actions.</li>" +
                                "</ul>" +
                                "This tutorial has introduced the typical usage of WepSIM for students and teachers. Enjoy WepSIM!" +
                                "</h5>"

    };


i18n_eltos['tutorial_welcome'] = {

                 "title_0":       "Welcome to the WepSIM simulator!",
                 "message_0":     "<center><img alt='wepsim screenshot' src='images/simulator/simulator012.jpg' style='max-width:100%; max-height:40vh;'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "This brief tutorial is going to show you how to:" +
                                  "<ol>" +
                                  "<li><a href='#' onclick='sim_tutorial_goframe(\"welcome\",0,1);'>Load an example.</a></li>" +
                                  "<li><a href='#' onclick='sim_tutorial_goframe(\"welcome\",0,2);'>Execute an example.</a></li>" +
                                  "<li><a href='#' onclick='sim_tutorial_goframe(\"welcome\",0,3);'>Configure the simulation.</a></li>" +
                                  "<li><a href='#' onclick='sim_tutorial_goframe(\"welcome\",0,4);'>Get help.</a></li>" +
                                  "</ol>" +
                                  "</h5>",

                 "title_1":       "How to load some example.",
                 "message_1":     "<center><img alt='wepsim screenshot' src='images/welcome/example_usage.gif' style='max-width:100%; max-height:60vh'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "Click in the 'example' button, then click in the example 'title' name.<br>" +
                                  "Then the example for microcode and assembly is loaded and microcompiled and compiled.<br>" +
                                  "<br>" +
                                  "</h5>",

                 "title_2":       "How to execute an example.",
                 "message_2":     "<center><img alt='wepsim screenshot' src='images/welcome/simulation_xinstruction.gif' style='max-width:100%; max-height:60vh'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "Click on next instruction/microinstruction to execute step by step. <br>" +
		                  "Click on run button to execute until the first breakpoint or the end of the assembly program." +
                                  "<br>" +
                                  "</h5>",

                 "title_3":       "How to configure WepSIM.",
                 "message_3":     "<center><img alt='wepsim screenshot' src='images/welcome/config_usage.gif' style='max-width:100%; max-height:60vh'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "Click in the 'configuration' button and users are able to customize different parts of WepSIM." +
                                  "<br>" +
                                  "</h5>",

                 "title_4":       "How to get the basic help.",
                 "message_4":     "<center><img alt='wepsim screenshot' src='images/welcome/help_usage.gif' style='max-width:100%; max-height:60vh'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "Please click in the green 'help' button to reach the help dialog.<br>" +
                                  "You are able to switch idiom (Spanish/English), go to the help index, or close the help dialog." +
                                  "<br>" +
                                  "</h5>",

                 "title_5":       "Welcome to WepSIM!",
                 "message_5":     "<center><img alt='wepsim screenshot' src='images/welcome/help_usage.gif' style='max-width:100%; max-height:60vh'></center>" +
                                  "<p>" +
                                  "<h5>" +
                                  "Please explorer the help sections for more information. <br>" +
                                  "If you click on the end button of this tutorial, WepSIM is going to load the first example for you. Enjoy!" +
                                  "<br>" +
                                  "</h5>"

};


#
# print translation
#
def print_content(L_D, C_N):
    fn = L_D + "/" + C_N + ".js" ;
    f  = open(fn, "w+") ;

    # + print header
    f.write("/*\n") ;
    f.write(" *  Copyright 2015-2019 Felix Garcia Carballeira, Alejandro Calderon Mateos, Javier Prieto Cepeda, Saul Alonso Monsalve\n") ;
    f.write(" *\n") ;
    f.write(" *  This file is part of WepSIM.\n") ;
    f.write(" *\n") ;
    f.write(" *  WepSIM is free software: you can redistribute it and/or modify\n") ;
    f.write(" *  it under the terms of the GNU Lesser General Public License as published by\n") ;
    f.write(" *  the Free Software Foundation, either version 3 of the License, or\n") ;
    f.write(" *  (at your option) any later version.\n") ;
    f.write(" *\n") ;
    f.write(" *  WepSIM is distributed in the hope that it will be useful,\n") ;
    f.write(" *  but WITHOUT ANY WARRANTY; without even the implied warranty of\n") ;
    f.write(" *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n") ;
    f.write(" *  GNU Lesser General Public License for more details.\n") ;
    f.write(" *\n") ;
    f.write(" *  You should have received a copy of the GNU Lesser General Public License\n") ;
    f.write(" *  along with WepSIM.  If not, see <http://www.gnu.org/licenses/>.\n") ;
    f.write(" *\n") ;
    f.write(" */\n") ;
    f.write("\n") ;

    # + print object name
    aa = C_N.replace('-','_') ;
    f.write("\n") ;
    f.write("    i18n.eltos." + aa + "." + L_D + " = {\n") ;
    f.write("\n") ;

    # + translate...
    try:
        translation_list = []
        translation_origin = []
        for key in i18n_eltos[aa]:
            translation_list.append(i18n_eltos[aa][key])
            translation_origin.append(key.replace("'", "\\'"))

        translator   = Translator() ;
        translations = translator.translate(translation_list, dest=L_D)

        for index in range(len(translation_origin)):
            translation_destination = translations[index].text.replace("'", "\\'") ;
            f.write("\t\t'" + translation_origin[index] + "':\t\t'" + translation_destination + "',\n") ;
    except Exception as e:
        print("\tERROR: " + str(e))
        #print("translation list:")
        #print(translation_list)

    # + print last lines
    f.write("\t\t'_last_':\t\t'_last_'\n") ;
    f.write("\n") ;
    f.write("    };\n") ;
    f.write("\n") ;

    f.close() ;


#
# Check params
#
if (len(sys.argv) < 2 or len(sys.argv) > 3):
    print("") ;
    print("  Usage:") ;
    print("  > " + sys.argv[0] + " <language> [<component>]") ;
    print("    * <languaje>:  it, es, en, hi, ...") ;
    print("    * <component>: cfg, dialogs, examples, gui, help, ...") ;
    print("") ;
    print("  Dependency:") ;
    print("  > pip install googletrans") ;
    print("    * googletrans project (https://pypi.org/project/googletrans/):") ;
    print("") ;
    sys.exit(0)

# + define elements
L_D     = sys.argv[1] ;
L_COMPO = [ "cfg", "dialogs", "examples", "gui", "help", "states",
            "tour-intro",  "tutorial-simpleusage", "tutorial-welcome" ] ;

# + directory
print("Directory for " + L_D + "...")
if not os.path.exists(L_D):
    os.mkdir(L_D) ;
open(L_D + "/index.html", 'a').close() ;

# + files
if (len(sys.argv) == 3):
    print("File for " + sys.argv[2] + "...") ;
    print_content(L_D, sys.argv[2]) ;
    sys.exit(0) ;

for F1 in L_COMPO:
    print("File for " + F1 + "...") ;
    print_content(L_D, F1) ;

# + the end
sys.exit(0) ;
