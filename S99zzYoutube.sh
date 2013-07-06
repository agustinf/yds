#!/bin/sh

start() {
 python /volume1/homes/agustin/main.py &
  return 0
  }
  
  stop() {
   killall beet
   return 0
   }
   
   case "$1" in
   start)
     start
      ;;
   stop)
     stop
         ;;
   restart)
      stop
      start
         ;;
       *)
     exit 1
     esac