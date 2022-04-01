XButton1::
	loop
	{
		if getkeystate("XButton1", "p")
		{
			Send {Volume_Down}
			sleep, 125
		}
		else
		{
		break
		}
	}
return

XButton2::
	loop
	{
		if getkeystate("XButton2", "p")
		{
			Send {Volume_Up}
			sleep, 125
		}
		else
		{
		break
		}
	}