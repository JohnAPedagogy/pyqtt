class SciNot:
  def __init__(self, val):
    self.val=val
  
  def vsign(self):
    if self.val<0:
      return -1
    else:
      return 1
  
  def esign(self):
    val=abs(self.val)
    if val>=1:
      return 1
    else:
      return -1
  
  def xval(self):
    esgn=esign(self.val)
    val=abs(self.val)
    mult= 0
    mr=val*10.0**mult
    if mr>=1 or mr<10:
      return 0
    while mr<1 or mr>=10:
      if esgn==1:
        mult-= 1
      else:
        mult+= 1
      mr=val*10.0**mult
    return mul
    
  def snot(self):
  	return self.val * pow(10,xval())

  def toString(self):    if (xval()==0):
      return str(self.val)    else:	      return str(snot())+"E"+(esign()*abs(xval()))

class EngNot(SciNot):
  def __init__(self, val):
    SciNot.__init__(val)

  def toString(self):
    if (xval()==0):
      return str(self.val)
    else:
      x = -1*xval()
      not="";
      mult=0;
      if x==20:
        not="E"
        mult=100      elif x==19:
        not="E"
        mult=10;
	    			break;	
	    		case 18:
	    			not="E";
	    			mult=1;	
	    			break;	
	    		case 17:
	    			not="P";
	    			mult=100;
	    			break;	
	    		case 16:
	    			not="P";
	    			mult=10;
	    			break;	
	    		case 15:
	    			not="P";
	    			mult=1;	
	    			break;	
	    		case 14:
	    			not="T";
	    			mult=100;
	    			break;	
	    		case 13:
	    			not="T";
	    			mult=10;
	    			break;	
	    		case 12:
	    			not="T";
	    			mult=1;	
	    			break;	
	    		case 11:
	    			not="G";
	    			mult=100;
	    			break;	
	    		case 10:
	    			not="G";
	    			mult=10;
	    			break;	
	    		case 9:
	    			not="G";
	    			mult=1;	
	    			break;	
	    		case 8:
	    			not="M";
	    			mult=100;
	    			break;	
	    		case 7:
	    			not="M";
	    			mult=10;
	    			break;	
	    		case 6:
	    			not="M";
	    			mult=1;	
	    			break;	
	    		case 5:
	    			not="k";
	    			mult=100;
	    			break;	
	    		case 4:
	    			not="k";
	    			mult=10;
	    			break;	
	    		case 3:
	    			not="k";
	    			mult=1;	
	    			break;	
	    		case 2:
	    			not="";
	    			mult=100;
	    			break;	
	    		case 1:
	    			not="";
	    			mult=10;
	    			break;	
	    		case -1:
	    			not="m";
	    			mult=100;	
	    			break;	
	    		case -2:
	    			not="m";
	    			mult=10;
	    			break;	
	    		case -3:
	    			not="m";
	    			mult=1;
	    			break;	
	    		case -4:
	    			not="u";
	    			mult=100;	
	    			break;	
	    		case -5:
	    			not="u";
	    			mult=10;
	    			break;	
	    		case -6:
	    			not="u";
	    			mult=1;
	    			break;	
	    		case -7:
	    			not="n";
	    			mult=100;	
	    			break;	
	    		case -8:
	    			not="n";
	    			mult=10;
	    			break;	
	    		case -9:
	    			not="n";
	    			mult=1;
	    			break;	
	    		case -10:
	    			not="p";
	    			mult=100;	
	    			break;	
	    		case -11:
	    			not="p";
	    			mult=10;
	    			break;	
	    		case -12:
	    			not="p";
	    			mult=1;
	    			break;	
	    		case -13:
	    			not="f";
	    			mult=100;	
	    			break;	
	    		case -14:
	    			not="f";
	    			mult=10;
	    			break;	
	    		case -15:
	    			not="f";
	    			mult=1;
	    			break;	
	    		case -16:
	    			not="a";
	    			mult=100;	
	    			break;	
	    		case -17:
	    			not="a";
	    			mult=10;
	    			break;	
	    		case -18:
	    			not="a";
	    			mult=1;
	    			break;	
	    		default:
	    			not="ERROR!";
	    			break;	
	    	}
	    	if (not.equals("ERROR!"))
	    		return "Value not within MAX Range";
	    	else
			return	String.valueOf(snot()*mult)+not;

   