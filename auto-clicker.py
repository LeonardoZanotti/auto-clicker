import pyautogui, time, sys

def main():
	if (len(sys.argv) != 4):
		print('Use: python3.7 auto-clicker.py <button> <time between clicks> <num of clicks>')
		return

	button = sys.argv[1]
	seconds = int(sys.argv[2])
	num = int(sys.argv[3])

	if (button == 'left'):
		for i in range(num):
			time.sleep(seconds)
			pyautogui.leftClick()
	elif (button == 'right'):
		for i in range(num):
			time.sleep(seconds)
			pyautogui.rightClick()
	else:
		print('Use: python3.7 auto-clicker.py <button> <time between clicks> <num of clicks>')
		return

if __name__ == '__main__':
	main()