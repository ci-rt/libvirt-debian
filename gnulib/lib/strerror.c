/* -*- buffer-read-only: t -*- vi: set ro: */
/* DO NOT EDIT! GENERATED AUTOMATICALLY! */
/* strerror.c --- POSIX compatible system error routine

   Copyright (C) 2007-2011 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU Lesser General Public License as published by
   the Free Software Foundation; either version 2.1 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

#include <config.h>

/* Specification.  */
#include <string.h>

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

#include "intprops.h"
#include "verify.h"

/* Use the system functions, not the gnulib overrides in this file.  */
#undef sprintf

#include "strerror-impl.h"
