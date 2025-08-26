from random import randint
from time import sleep

def grid(n):
  l=[]
  h={}
  temp=1
  for i in range (1,n+1):
    row=[]
    for j in range(1,n+1):
      row.append(temp)
      h[temp]=(j,i)
      temp+=1
    if i%2==0:
      row=row[::-1]
    l.append(row) 
  return l,h

def player(p_size):
  h={}
  f={}
  for i in range(p_size):
    name=input('enetr ur player id: ')
    h[name]=0
    f[name]=()
  return h,f,f

def summary(pos_his,dice_his,cur_pos):
  s=input('enter player id : ')
  cor_his=[hash_grid[x] for x in pos_his[s]]
  print(f'SUMMARY OF PLAYER {s}\nwin_status={cur_pos[s]}\nposition_his={pos_his[s]}\ncordinate_his={cor_his}\ndice_his={dice_his[s]}')


n=int(input('enter the grid size: '))
main_grid,hash_grid=grid(n)
p_size=int(input('enter no of players: '))
cur_pos,dice_his,pos_his=player(p_size)

while True:
  #game
  for i in cur_pos:
    d=randint(1,6)
    #print(f'player {i} rolled {d}')
    cur_pos[i]+=d
    if cur_pos[i]==n*n:
        print(f'game over player {i} has won!')
        break
    for j in cur_pos:     
      if cur_pos[j]==cur_pos[i] and i!=j:
        print(f'player {i} killed player {j} at {hash_grid[cur_pos[i]]}')
        cur_pos[j]=0
        sleep(1)
    if cur_pos[i] > n*n:
      cur_pos[i]-=d
    pos_his[i]+=(cur_pos[i],)
    dice_his[i]+=(d,)

  #game over
  if cur_pos[i]==n*n:
    for k in cur_pos:
      cur_pos[k]=0
      if k==i:
        cur_pos[k]=1
    break 

while True:

  print('1.analysis\n2.exit')
  check=input('enter choice: ')
  match check:
    case '1':
      summary(pos_his,dice_his,cur_pos)
    case '2':
      break
    case _ :
      print('entr a valid choice..')
