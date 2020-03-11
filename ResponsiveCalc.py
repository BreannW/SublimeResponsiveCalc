import sublime
import sublime_plugin
import re


class calcwidthCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		window.run_command("show_panel", {"panel": "console"})

		for region in self.view.sel():  #get user selection
			if not region.empty():  #if selection not empty then
				selection = self.view.substr(region).splitlines()  #assign selection variable the selected 
				print('View Widths:')	
				viewWidthsList = []
				classList = []
				for line in selection:
					className = re.match('(\..*){', line)# Determine if it's a class name
					idName= re.match('(\#.*){', line)# Determine if it's an ID name
					matches = re.findall('(\d*)px', line)# Determine if there are matches

					attr = re.match('^(.(?!(\d*px)))*:', line)# Determine the attributes

					if className:
						#if it's a class, add it to the viewWidthsList and close the previous class with a }
						viewWidthsList.append('}\n'+ className.group())
				
					if idName:
						viewWidthsList.append('}\n'+ idName.group())

					if matches:
						valList = []#val list stores values when we have cases like padding where you may have more than 1 value (Padding: 20px 30px 30px)
						attr = attr.group()#gets the attribute we're calculating values for
						for match in matches:
							originalNumber = int(match)

							viewWidths = round((originalNumber/1366)*100,4)
							newPixVal = round((viewWidths*1280)/100,4)
			
							viewWidths =str(viewWidths) + 'vw'
							
							valList.append(viewWidths)#put all values in the valList 
							
						viewWidthsList.append(attr+ ' '.join(valList)+';')#add the attribute, join the values in valList, and append it all to viewWidthsList
				
				print("\n".join(viewWidthsList) + '\n}')
					
				print('Pixel Widths:')	
				pixWidthsList = []
				for line in selection:
					className = re.match('(\..*){', line)
					matches = re.findall('(\d*)px', line)
					attr = re.match('^(.(?!(\d*px)))*:', line)

					if className:
						#close the previous class with a }
						pixWidthsList.append('}\n'+ className.group())

					if matches:
						pixValList = []
						attr = attr.group()
						for match in matches:
							originalNumber = int(match)

							viewWidths = round((originalNumber/1366)*100,4)
							
							newPixVal = round((viewWidths*1280)/100,4)
							newPixVal = str(newPixVal) + 'px'
							
							pixValList.append(newPixVal)

						pixWidthsList.append(attr+ ' '.join(pixValList)+';')
				
				print('\n'.join(pixWidthsList)+ '\n}')

class calcmobileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		window.run_command("show_panel", {"panel": "console"})
		for region in self.view.sel():  #get user selection
			if not region.empty():  #if selection not empty then
				selection = self.view.substr(region).splitlines()  #assign s variable the selected 
				print('Mobile VW:')	
				viewWidthsList = []
				classList = []
				for line in selection:
					className = re.match('(\..*){', line)
					idName= re.match('(\#.*){', line)
					matches = re.findall('(\d*)px', line)
					attr = re.match('^(.(?!(\d*px)))*:', line)

					if className:
						#close the previous class with a }
						viewWidthsList.append('}\n'+ className.group())

					if idName:
						viewWidthsList.append('}\n'+ idName.group())

				
					if matches:
						valList = []
						attr = attr.group()
						for match in matches:
							originalNumber = int(match)

							viewWidths = round((originalNumber/750)*100,4)
			
							viewWidths =str(viewWidths) + 'vw'
							
							valList.append(viewWidths)
							
						viewWidthsList.append(attr+ ' '.join(valList)+';')
				
				print("\n".join(viewWidthsList) + '\n}')
