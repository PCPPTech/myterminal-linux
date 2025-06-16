import os
from color_codes import *


try:
	from tkinter import *
except ModuleNotFoundError:
	print(f"{bg_green}{black}[INFO]{reset} since you dont have tkinter installed,")
	print(f"{bg_green}{black}[INFO]{reset} we are gonna attempt to use the command `sudo apt install python3-tk`.")
	print(f"{bg_red}{black}[INPUT]{reset} are you okay with that? (y/n, default: y)")
	ans = input("> ").lower()
	if ans == "" or ans == "y":
		os.system("sudo apt install python3-tk")
	else:
		print("Quitting installation process...")
		quit()


installation_path = os.path.expanduser('~')
def main():
	def submit(event):
		global installation_path
		installation_path = given_installation_path_entry.get()
		inst_gui.destroy()

		# check if the installation path is valid
		try:
			os.chdir(installation_path)
		except FileNotFoundError:
			err = Tk()
			err.title("Installation - Error")
			err.configure(bg='red')
			err.resizable(False, False)

			label = Label(err, text="Given installation path is invalid. Please change your answer.", font=("Arial", 15))
			label.pack()
			err.mainloop()

	inst_gui = Tk()
	# centrify inst_gui
	w = 800
	h = 500
	sw = inst_gui.winfo_screenwidth()
	sh = inst_gui.winfo_screenheight()

	x = (sw-w) // 2
	y = (sh-h) // 2
	inst_gui.geometry(f"{w}x{h}+{x}+{y}")
	inst_gui.resizable(False, False)
	inst_gui.title("myterminal (linux) installation path")
	label = Label(inst_gui, text="Please choose the installation path", font=("Arial", 12))
	given_installation_path_entry = Entry(inst_gui, font=("Arial", 15, 'bold'), width=250)
	given_installation_path_entry.insert(0, installation_path)
	#pack widgets
	label.pack()
	given_installation_path_entry.pack()

	# binds
	given_installation_path_entry.bind("<Return>", submit)

	inst_gui.mainloop()

if __name__ == '__main__':
	main()
	with open(f"{os.path.expanduser}/mtpaths.txt", "a+") as file:
		file.write(installation_path)
	os.chdir(installation_path)
	os.mkdir(".mt")
	os.mkdir(".mt/home")
	with open(".mt/home/readme.txt", "a+") as f:
		f.write("Hello! Eidnoxon (PCPPTech) speaking.\n")
		f.write("Copy and pasted myTerminal code into this, with the slight\n")
		f.write("Modification of linux operating system's liking.\n")
		f.write("If any error occurs while using this version, PLEASE,\n")
		f.write(f"Don't hesitate to contact me on Discord: {red}eidnoxon{reset} !!!")