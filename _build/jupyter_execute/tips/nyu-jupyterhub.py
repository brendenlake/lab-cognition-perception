#!/usr/bin/env python
# coding: utf-8

# # NYU JupyterHub Setup

# ```{note}
# This document authored by [Denis Pelli](https://psych.nyu.edu/pelli/) and [Todd M. Gureckis](http://gureckislab.org/~gureckis) with help from Sergey Samsonau and Eric Borenstein.
# ```

# Psychology is reorganizing the labs for cognition and perception. Todd Gureckis has developed several easy python Jupyter notebooks to introduce undergraduates to basic concepts, like hypothesis testing.
# http://gureckislab.org/courses/fall19/labincp/chapters/09/00-hypothesistesting.html
# Here is what you need to do to use these notebooks in your class. You’ll need to create (currently free) accounts at the High Performance Computing center (HPC), and install necessary python modules.

# ## Overview and FAQ

# - https://sites.google.com/a/nyu.edu/nyu-hpc/services/resources-for-classes/rc-jupyterhub
# - https://sites.google.com/a/nyu.edu/nyu-hpc/services/resources-for-classes/rc-jupyterhub/faq
# - You can send questions by emailing hpc@nyu.edu

# ## Request Account

# Apply for an account for yourself and students:
# https://sites.google.com/a/nyu.edu/nyu-hpc/services/resources-for-classes/rc-jupyterhub/intake-form
# 
# Wait, about a day, for an email announcing accounts for you and your class. It will provide an instructor link (for you and TAs) and a student link for all your students.

# ## Read the manual
# Log in as the instructor and read the ~/tuning/MANUAL.html

# ## Add students
# 
# There are several ways to add students. The recommended way is to add their NYU ids to the white list.
# Edit the file /tuning/settings.txt, and add the student NYU IDs to this line:
# STUD_WHITELIST:xx123,xy123,xx234,xx234
# (Those IDs are for a hypothetical class. Yours will be different.)
# 
# ## Turbo 
# Before doing custom software installations (see below), turn on TURBO mode, as explained in the MANUAL. TURBO temporarily increases your resources, hopefully enough to allow installations, and turns itself off some hours later. You have to wait around 10 m or more for your request to be acted on. I’m not sure how you can tell that you’re in TURBO mode. Without TURBO, our every attempt to install died with a “Kill” error message. Even with TURBO, some installation attempts were Killed. For example, trying to install two scikit modules in one install failed, but succeeded when installed in separate commands.
# 

# ## Install 
# 
# As explained in MANUAL, use Terminal to load Python modules. These are commands to load the modules needed by Todd Gureckis’s teaching notebooks for Cognition and Perception:
# 
# ```
# conda create --name perception python=3.7
# conda install -n perception ipykernel
# conda activate perception
# conda install -c conda-forge pandas
# conda install -c conda-forge seaborn
# conda install scikit-learn
# conda install scikit-image
# conda install colorlover matplotlib pingouin
# pip install celluloid
# ```
# 
# To do further installations at a later time, begin with
# conda activate perception
# 

# ## Persistant storage for students
# 
# The default is for student accounts to remember nothing from session to session. There's an option one can edit to make their changes persistent (until end of semester).  Edit the file `~/tuning/settings.txt` and change this
# `PERSISTENTSTORAGE:no`
# to
# `PERSISTENTSTORAGE:yes`
# Save the file.

# ## Change kernel
# 
# Every time you or a student spawns a new session, to use the modules you installed above, you and each student must use the Kernel menu to select Change Kernel, and select the “Python [env:Perception]” kernel.

# ## Shared folder is read-only
# 
# The shared folder helpfully allows the instructor(s) to provide files for student use. However, the student have only read access to that folder, so if you want them to modify anything, they’ll first need to copy the file outside of that folder.

# In[ ]:




