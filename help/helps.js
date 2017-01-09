
    var helps = new Array();

    helps.push({
                     id:          "simulator",
                     title:       "Simulator usage",
                     type:        "relative",
                     reference:   "#help_simulator_screens",
                     description: "Description of how the simulator works.<br>"
                  });

    helps.push({
                     id:          "microcode",
                     title:       "Microcode format",
                     type:        "relative",
                     reference:   "#help_firmware_format",
                     description: "Syntax of the microcode used.<br>"
                  });

    helps.push({
                     id:          "assembly",
                     title:       "Assembly format",
                     type:        "relative",
                     reference:   "#help_assembly_format",
                     description: "Syntax of the assembly elements.<br>"
                  });

    helps.push({
                     id:          "architecture",
                     title:       "Simulator architecture",
                     type:        "relative",
                     reference:   "#help_simulator_arch",
                     description: "Description of the simulator architecture.<br>"
                  });

    helps.push({
                     id:          "architecture",
                     title:       "Hardware summary",
                     type:        "code",
                     reference:   "$(\'#help1_ref\').data(\'relative\',\'\');" +
                                  "$(\'#iframe_help1\').html(\'<object id=svg_p2 data=\\'images/cpu6.svg?time=20170108\\' type=image/svg+xml>Your browser does not support SVG</object>\');" +
                                  "$(\'#help1\').trigger(\'updatelayout\');" +
                                  "$(\'#help1\').popup(\'reposition\', {positionTo: \'window\'});" +
                                  "$(\'#help1\').popup(\'open\');",
                     description: "Reference card of the elemental processor hardware simulated.<br>"
                  });

    helps.push({
                     id:          "simulator",
                     title:       "Signal dependencies",
                     type:        "code",
                     reference:   "$(\'#iframe_help1\').html(\'<div id=depgraph1>...</div>\'); " + 
                                  "$(\'#help1\').trigger(\'updatelayout\');" +
                                  "$(\'#help1\').popup(\'reposition\', {positionTo: \'window\'});" +
                                  "$(\'#help1\').popup(\'open\');" +
                                  "show_visgraph(jit_fire_dep, jit_fire_order);",
                     description: "Graph of the signal dependencies (need several seconds to display).<br>"
                  });

