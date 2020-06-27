using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string keyPressed, out int x, out int y)
    {
      x=0;
      y=0;
      switch (keyPressed)
      {
        case "LeftArrow":
        x-=1;
        break;
        case "RightArrow":
        x+=1;
        break;
        case "UpArrow":
        y-=1;
        break;
        case "DownArrow":
        y+=1;
        break;
        default:   
        x+=0;
        y+=0;
        break;
      }
    }
    public new static char UpdateCursor(string keyPressed)
    {
      char direction='0';
      switch (keyPressed)
      {
        case "LeftArrow":
        return direction='<';
        break;
        case "RightArrow":
        return direction='>';
        break;
        case "UpArrow":
        return direction ='^';
        break;
        case "DownArrow":
        return direction='v';
        break;
      }
    return direction;
    }
    public new static int KeepInBounds(int coordinate, int maxCoord){
      if(coordinate>maxCoord){
  //character is sent to the initial position(0,0)
      return 0;
      }else if(coordinate<0){
        return maxCoord;
      }
      else{
        return coordinate;
      }
    }
    public new static bool DidScore(int charX, int charY, int fruitX, int fruitY)
    {
      if(charX==fruitX && charY==fruitY){
        return true;
      }else{
        return false;
      }
    }
  }
}