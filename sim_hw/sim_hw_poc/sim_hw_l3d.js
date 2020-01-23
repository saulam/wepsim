/*      
 *  Copyright 2015-2020 Felix Garcia Carballeira, Alejandro Calderon Mateos, Javier Prieto Cepeda, Saul Alonso Monsalve
 *
 *  This file is part of WepSIM.
 * 
 *  WepSIM is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  WepSIM is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public License
 *  along with WepSIM.  If not, see <http://www.gnu.org/licenses/>.
 *
 */


	/*
	 *  L3D
	 */

        poc_components.L3D = {
		                  name: "L3D", 
		                  version: "1", 
		                  abilities:    [ "3DLED" ],

		                  // ui: details
		                  details_name: [ "3DLED" ],
                                  details_fire: [ [] ],

		                  // state: write_state, read_state, get_state
		                  write_state: function ( vec ) {
						  return vec;
				               },
		                  read_state:  function ( o, check ) {
                                                  return false ;
				               },
		                  get_state:   function ( reg ) {
					          return null ;
				               },

		                  // native: get_value, set_value
                                  get_value:   function ( elto ) {
						    var associated_state = simhw_internalState_get('io_hash',elto) ;
						    var value = (get_value(simhw_sim_state(associated_state)) >>> 0) ;

						    set_value(simhw_sim_state('BUS_AB'), elto) ;
						    set_value(simhw_sim_signal('L3DR'), 1) ;
						    compute_behavior("FIRE L3DR") ;
						    value = get_value(simhw_sim_state('BUS_DB')) ;

						    return value ;
                                               },
                                  set_value:   function ( elto, value ) {
						    var associated_state = simhw_internalState_get('io_hash',elto) ;
						    set_value(simhw_sim_state(associated_state), value) ;

						    set_value(simhw_sim_state('BUS_AB'), elto) ;
						    set_value(simhw_sim_state('BUS_DB'), value) ;
						    set_value(simhw_sim_signal('L3DW'), 1) ;
						    compute_behavior("FIRE L3DW") ;

						    return value ;
                                               }
                            	};


	/*
	 *  States - L3D parameters
	 */

        poc_internal_states.l3d_state = [] ;
        poc_internal_states.l3d_state[0]  = { active: false } ;
        poc_internal_states.l3d_state[1]  = { active: false } ;
        poc_internal_states.l3d_state[2]  = { active: false } ;
        poc_internal_states.l3d_state[3]  = { active: false } ;
        poc_internal_states.l3d_state[4]  = { active: false } ;
        poc_internal_states.l3d_state[5]  = { active: false } ;
        poc_internal_states.l3d_state[6]  = { active: false } ;
        poc_internal_states.l3d_state[7]  = { active: false } ;
        poc_internal_states.l3d_state[8]  = { active: false } ;
        poc_internal_states.l3d_state[9]  = { active: false } ;
        poc_internal_states.l3d_state[10] = { active: false } ;
        poc_internal_states.l3d_state[11] = { active: false } ;
        poc_internal_states.l3d_state[12] = { active: false } ;
        poc_internal_states.l3d_state[13] = { active: false } ;
        poc_internal_states.l3d_state[14] = { active: false } ;
        poc_internal_states.l3d_state[15] = { active: false } ;
        poc_internal_states.l3d_state[16] = { active: false } ;
        poc_internal_states.l3d_state[17] = { active: false } ;
        poc_internal_states.l3d_state[18] = { active: false } ;
        poc_internal_states.l3d_state[19] = { active: false } ;
        poc_internal_states.l3d_state[20] = { active: false } ;
        poc_internal_states.l3d_state[21] = { active: false } ;
        poc_internal_states.l3d_state[22] = { active: false } ;
        poc_internal_states.l3d_state[23] = { active: false } ;
        poc_internal_states.l3d_state[24] = { active: false } ;
        poc_internal_states.l3d_state[25] = { active: false } ;
        poc_internal_states.l3d_state[26] = { active: false } ;

        var L3DSR_ID   = 0x2100 ;
        var L3DCR_ID   = 0x2104 ;
        var L3DDR_ID   = 0x2108 ;

        poc_internal_states.io_hash[L3DSR_ID] = "L3DSR" ;
        poc_internal_states.io_hash[L3DCR_ID] = "L3DCR" ;
        poc_internal_states.io_hash[L3DDR_ID] = "L3DDR" ;


        /*
         *  States
         */

        poc_states.L3DSR = { name: "L3DSR", verbal: "L3D State Register",
                             visible:false, nbits: "32", value: 0, default_value: 0, draw_data: [] };
        poc_states.L3DCR = { name: "L3DCR", verbal: "L3D Control Register",
                             visible:false, nbits: "32", value: 0, default_value: 0, draw_data: [] };
        poc_states.L3DDR = { name: "L3DDR", verbal: "L3D Data Register",
                             visible:false, nbits: "32", value: 0, default_value: 0, draw_data: [] };


        /*
         *  Signals
         */

         poc_signals.L3D_L3DR   = { name: "L3D_L3DR", 
                                    visible: true, type: "L", value: 0, default_value:0, nbits: "1", 
                                    behavior: ["NOP", "L3D_L3DR BUS_AB BUS_DB L3DSR L3DCR L3DDR CLK; FIRE M1"],
                                    fire_name: ['svg_p:tspan4173'], 
                                    draw_data: [[], ['svg_p:path3795', 'svg_p:path3733']], 
                                    draw_name: [[], []]};

         poc_signals.L3D_L3DW   = { name: "L3D_L3DW", 
                                    visible: true, type: "L", value: 0, default_value:0, nbits: "1", 
                                    behavior: ["NOP", "L3D_L3DW BUS_AB BUS_DB L3DSR L3DCR L3DDR CLK; FIRE M1"],
                                    fire_name: ['svg_p:text3785-0-6-0-5-5'], 
                                    draw_data: [[], ['svg_p:path3805', 'svg_p:path3733']], 
                                    draw_name: [[], []]};


        /*
         *  Syntax of behaviors
         */

        poc_behaviors.L3D_L3DR      = { nparameters: 7,
                                        types: ["E", "E", "E", "E", "E", "E"],
                                        operation: function (s_expr) 
                                                   {
                                                      var bus_ab = get_value(poc_states[s_expr[1]]) ;
                                                      var iosr   = get_value(poc_states[s_expr[3]]) ;
                                                      var iocr   = get_value(poc_states[s_expr[4]]) ;
                                                      var iodr   = get_value(poc_states[s_expr[5]]) ;

                                                      if (bus_ab == L3DSR_ID) 
                                                          set_value(poc_states[s_expr[2]], iosr);
                                                      if (bus_ab == L3DCR_ID) 
                                                          set_value(poc_states[s_expr[2]], iocr);
                                                      if (bus_ab == L3DDR_ID) 
                                                          set_value(poc_states[s_expr[2]], iodr);

                                                      // get
                                                      if (bus_ab == L3DCR_ID) {
						          simcore_rest_call("L3D", "GET", "/get", {}) ; // TODO: {} -> { 'id': data }
						      }
                                                   },
                                           verbal: function (s_expr) 
                                                   {
                                                      var verbal = "" ;

                                                      var bus_ab = get_value(poc_states[s_expr[1]]) ;
                                                      var iosr   = get_value(poc_states[s_expr[3]]) ;
                                                      var iocr   = get_value(poc_states[s_expr[4]]) ;
                                                      var iodr   = get_value(poc_states[s_expr[5]]) ;

                                                      if (bus_ab == L3DSR_ID) 
                                                          verbal = "I/O device read at L3DSR of value " + iosr + ". " ;
                                                      if (bus_ab == L3DCR_ID) 
                                                          verbal = "I/O device read at L3DCR of value " + iocr + ". " ;
                                                      if (bus_ab == L3DDR_ID) 
                                                          verbal = "I/O device read at L3DDR of value " + iodr + ". " ;

                                                      return verbal ;
                                                   }
                                      };

        poc_behaviors.L3D_L3DW      = { nparameters: 7,
                                        types: ["E", "E", "E", "E", "E", "E"],
                                        operation: function (s_expr) 
                                                   {
                                                      var bus_ab = get_value(poc_states[s_expr[1]]) ;
                                                      var bus_db = get_value(poc_states[s_expr[2]]) ;

                                                      if ( (bus_ab != L3DSR_ID) &&
                                                           (bus_ab != L3DCR_ID) &&
                                                           (bus_ab != L3DDR_ID) )
                                                      {
                                                            return; 
                                                      }

                                                      if (bus_ab == L3DSR_ID) 
                                                          set_value(poc_states[s_expr[3]], bus_db);
                                                      if (bus_ab == L3DCR_ID) 
                                                          set_value(poc_states[s_expr[4]], bus_db);
                                                      if (bus_ab == L3DDR_ID) 
                                                          set_value(poc_states[s_expr[5]], bus_db);

                                                      // set
                                                      if (bus_ab == L3DCR_ID) 
						          simcore_rest_call("L3D", "GET", "/set", {}) ; // TODO: {} -> { 'id': data }
                                                   },
                                           verbal: function (s_expr) 
                                                   {
                                                      var verbal = "" ;
                                                      var bus_ab = get_value(poc_states[s_expr[1]]) ;
                                                      var bus_db = get_value(poc_states[s_expr[2]]) ;

                                                      if (bus_ab == L3DSR_ID) 
                                                          verbal = "I/O device write at L3DSR with value " + bus_db + ". " ;
                                                      if (bus_ab == L3DCR_ID) 
                                                          verbal = "I/O device write at L3DCR with value " + bus_db + ". " ;
                                                      if (bus_ab == L3DDR_ID) 
                                                          verbal = "I/O device write at L3DDR with value " + bus_db + ". " ;

                                                      return verbal ;
                                                   }
                                      };

        poc_behaviors.L3D_RESET    = { nparameters: 1,
                                       operation: function (s_expr) 
                                                  {
						     // reset events.l3d
                                                     poc_events.l3d = {} ;

						     // reset the I/O factory
						     for (var i=0; i<poc_internal_states.l3d_state.length; i++)
						     {
						          set_var(poc_internal_states.l3d_state[i].active, false);
						     }
                                                  },
                                          verbal: function (s_expr) 
                                                  {
                                                     return "Reset the I/O device. " ;
                                                  }
                                     };
