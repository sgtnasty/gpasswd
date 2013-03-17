#!/usr/bin/env python3
"""
	Helps you create a compliant password.
    Copyright (C) 2013  Ronaldo Nascimento <ronaldo1@users.sf.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from gi.repository import Gtk, Gdk
import random, string, math

class Handler:
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)
	
	def on_about_toolbutton_clicked(self, *args):
		ad = Gtk.AboutDialog()
		ad.set_program_name("GTK+ Password")
		ad.set_version("0.0.1")
		ad.set_copyright("(c) 2013 by Ronaldo Nascimento")
		ad.set_comments("Helps you create a compliant password.")
		ad.set_website("https://github.com/sgtnasty/gpasswd/wiki")
		ad.set_website_label("Homepage")
		ad.set_authors(["Ronaldo Nascimento"])
		#ad.set_logo()
		ad.set_license('Distributed under the GPL v3 license.\nhttp://www.gnu.org/licenses/gpl-3.0.html')
		ad.run()
		ad.destroy()
	
	def on_copy_toolbutton_clicked(self, *args):
		clipboard.set_text(result_entry.get_text(), -1)
		print("copied: ", result_entry.get_text())
	
	def on_preview_toolbutton_clicked(self, *args):
		dialog = Gtk.MessageDialog(window, 0, 
			Gtk.MessageType.WARNING,Gtk.ButtonsType.OK, 
			"Function Not Implemented")
		dialog.format_secondary_text(
			"Preview function is not implemented yet!")
		response = dialog.run()
		dialog.destroy()
		
	def on_random_toolbutton_clicked(self, *args):
		base_entry.set_text(random_string(12))
	
	def on_base_entry_changed(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))
		
	def on_capital_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encE_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encT_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encA_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encO_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encI_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_encS_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_append_checkbutton_toggled(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))

	def on_append_entry_changed(self, *args):
		result_entry.set_text(encode_string(base_entry.get_text()))
	
def random_string(length):
	return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(length))
	
def encode_string(base_string):
	if (encE_checkbutton.get_active()):
		enc = ''.join('3' * 2)
		emap = ''.maketrans("eE", enc)
		base_string = base_string.translate(emap)
	if (encT_checkbutton.get_active()):
		enc = ''.join('+' * 2)
		emap = ''.maketrans("tT", enc)
		base_string = base_string.translate(emap)
	if (encA_checkbutton.get_active()):
		enc = ''.join('@' * 2)
		emap = ''.maketrans("aA", enc)
		base_string = base_string.translate(emap)
	if (encO_checkbutton.get_active()):
		enc = ''.join('0' * 2)
		emap = ''.maketrans("oO", enc)
		base_string = base_string.translate(emap)
	if (encI_checkbutton.get_active()):
		enc = ''.join('|' * 2)
		emap = ''.maketrans("iI", enc)
		base_string = base_string.translate(emap)
	if (encS_checkbutton.get_active()):
		enc = ''.join('$' * 2)
		emap = ''.maketrans("sS", enc)
		base_string = base_string.translate(emap)
	if (append_checkbutton.get_active()):
		base_string = base_string + append_entry.get_text()
	if (capital_checkbutton.get_active()):
		base_string = base_string.capitalize()
	statusbar1.push(0, "Entropy: " + str(calculate_entropy(result_entry.get_text())))
	return base_string
	
def calculate_entropy(result_string):
	return len(result_string) * math.log(94) / math.log(2)

builder = Gtk.Builder()
builder.add_from_file("gpasswd.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
about_toolbutton = builder.get_object("about_toolbutton")
copy_toolbutton = builder.get_object("copy_toolbutton")
preview_toolbutton = builder.get_object("preview_toolbutton")
random_toolbutton = builder.get_object("random_toolbutton")
base_entry = builder.get_object("base_entry")
capital_checkbutton = builder.get_object("capital_checkbutton")
encE_checkbutton = builder.get_object("encE_checkbutton")
encT_checkbutton = builder.get_object("encT_checkbutton")
encA_checkbutton = builder.get_object("encA_checkbutton")
encO_checkbutton = builder.get_object("encO_checkbutton")
encI_checkbutton = builder.get_object("encI_checkbutton")
encS_checkbutton = builder.get_object("encS_checkbutton")
append_checkbutton = builder.get_object("append_checkbutton")
append_entry = builder.get_object("append_entry")
result_entry = builder.get_object("result_entry")
statusbar1 = builder.get_object("statusbar1")

window.show_all()

statusbar1.push(0, "Ready")
base_entry.set_text(random_string(12))

Gtk.main()
