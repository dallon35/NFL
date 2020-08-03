#got code from https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import random
import time

# { NFL Data Pull
teams = {'ARI': ('crd'), 'ATL': ('atl'), 'BAL': ('rav'), 'BUF': ('buf'), 'CAR': ('car'), 'CHI': ('chi'), 'CIN': ('cin'), 'CLE': ('cle'), 'DAL': ('dal'), 'DEN': ('den'), 'DET': ('det'), 'GB': ('gnb'), 'HOU': ('htx'), 'IND': ('clt'), 'JAX': ('jax'), 'KC': ('kan'), 'LAC': ('sdg'), 'LAR': ('ram'), 'MIA': ('mia'), 'MIN': ('min'), 'NE': ('nwe'), 'NO': ('nor'), 'NYG': ('nyg'), 'NYJ': ('nyj'), 'OAK': ('rai'), 'PHI': ('phi'), 'PIT': ('pit'), 'SF': ('sfo'), 'SEA': ('sea'), 'TB': ('tam'), 'TEN': ('oti'), 'WSH': ('was')}
for key,value in teams.items():
    tm = key.format(key)
    tm2 = value.format(value)
    url = 'https://www.pro-football-reference.com/teams/'+tm2+'/2019/gamelog/'
#    url = 'https://www.pro-football-reference.com/teams/'+tm2+'/2018/gamelog/'
#    url = 'https://www.pro-football-reference.com/teams/'+tm2+'/2017/gamelog/'
# }

    response = get(url)

    soup = BeautifulSoup(response.text, 'lxml') # Parse the HTML as a string

    table = soup.find_all('table')[0]
    if len(table.find_all('td')) < 16:
        table = soup.find_all('table')[1]
    else:
        table

    file_name = str(tm)+'2019'
    new_csv = "/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+file_name+".csv"

    n_columns = 0
    n_rows = 0
    column_names = []

    # Find number of rows and columns
    # we also find the column titles if we can
    for row in table.find_all('tr'):
        
        # Determine the number of rows in the table
        td_tags = row.find_all('td')
        if len(td_tags) > 0:
            n_rows+=1
            if n_columns == 0:
                # Set the number of columns for our table
                n_columns = len(td_tags)
                
        # Handle column names if we find them
        th_tags = row.find_all('th') 
        if len(th_tags) > 0 and len(column_names) == 0:
            for th in th_tags:
                column_names.append(th.get_text())

    # Safeguard on Column Titles
    #if len(column_names) > 0 and len(column_names) != n_columns:
    #    raise Exception("Column titles do not match the number of columns")

    columns = column_names if len(column_names) > 0 else range(0,n_columns)
    df = pd.DataFrame(columns = range(0,n_columns + 1), index = range(0,n_rows))

    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('th')
        for column in columns:
            df.iat[row_marker,column_marker] = column.get_text()
        column_marker = 1
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker,column_marker] = column.get_text()
            column_marker += 1
        if len(columns) > 0:
            row_marker += 1

    df.to_csv(path_or_buf = new_csv,index=False)
    print('New CSV File Created/Saved for '+str(file_name))
    d = random.uniform(1,5)
    time.sleep(d)

# Input/Sim {
import pandas as pd
# }

# Sim {
t_1 = ''
#teams = {'ARI'}
teams = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX', 'KC', 'LAC', 'LAR', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SEA', 'SF', 'TB', 'TEN', 'WSH']
p_score_r = 0
p_score_w = 0
p_score = 0
r_score_r = 0
r_score_w = 0
r_score = 0
f1_score = 0
nfl_cr = {}
for t_1 in teams:
    # Input/Sim {
    s = 17

    year = 2018
    y = str(year)
    yp = str(year - 1)
    # }

    # Sim {
    w = 0
    l = 0
    g = 1
    for g in range(g, s, 1):

        # Sim {
        t_1_m = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+y+".csv",usecols=[7])
        t_nm = t_1_m.iat[g-1,0]
        if t_nm == "Bye Week":
            g += 1

        t_1_s = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+y+".csv",usecols=[7])
        t_2_l = t_1_s.iat[g-1,0]

        t_2 = t_2_l.replace("Arizona Cardinals", "ARI").replace("Atlanta Falcons", "ATL").replace("Baltimore Ravens", "BAL").replace("Buffalo Bills", "BUF").replace("Carolina Panthers", "CAR").replace("Chicago Bears", "CHI").replace("Cincinnati Bengals", "CIN").replace("Cleveland Browns", "CLE").replace("Dallas Cowboys", "DAL").replace("Denver Broncos", "DEN").replace("Detroit Lions", "DET").replace("Green Bay Packers", "GB").replace("Houston Texans", "HOU").replace("Indianapolis Colts", "IND").replace("Jacksonville Jaguars", "JAX").replace("Kansas City Chiefs", "KC").replace("Los Angeles Chargers", "LAC").replace("Los Angeles Rams", "LAR").replace("Miami Dolphins", "MIA").replace("Minnesota Vikings", "MIN").replace("New England Patriots", "NE").replace("New Orleans Saints", "NO").replace("New York Giants", "NYG").replace("New York Jets", "NYJ").replace("Oakland Raiders", "OAK").replace("Philadelphia Eagles", "PHI").replace("Pittsburgh Steelers", "PIT").replace("Seattle Seahawks", "SEA").replace("San Francisco 49ers", "SF").replace("Tampa Bay Buccaneers", "TB").replace("Tennessee Titans", "TEN").replace("Washington Redskins", "WSH")

        h_1_s = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+y+".csv",usecols=[6])
        h = h_1_s.iat[g-1,0]
        if h is "@":
            h_1 = 0
            h_2 = 3.5
        else:
            h_1 = 3.5
            h_2 = 0
        # }

        # Input/Sim {
        pyp_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+yp+".csv",usecols=[8]).fillna(0)
        py_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+y+".csv",usecols=[8]).fillna(0)
        oyp_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+yp+".csv",usecols=[9]).fillna(0)
        oy_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_1+y+".csv",usecols=[9]).fillna(0)
        pyp_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_2+yp+".csv",usecols=[8]).fillna(0)
        py_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_2+y+".csv",usecols=[8]).fillna(0)
        oyp_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_2+yp+".csv",usecols=[9]).fillna(0)
        oy_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/NFL_Team_Data/"+t_2+y+".csv",usecols=[9]).fillna(0)

        mmpyp_1 = pyp_1.mean() * ((s-g)/s) + pyp_1.median() * (g/s)
        sdpyp_1 = pyp_1.std()
        mmpy_1 = py_1.mean() * ((s-g)/s) + py_1.median() * (g/s)
        sdpy_1 = py_1.std()
        mmoyp_1 = oyp_1.mean() * ((s-g)/s) + oyp_1.median() * (g/s)
        sdoyp_1 = oyp_1.std()
        mmoy_1 = oy_1.mean() * ((s-g)/s) + oy_1.median() * (g/s)
        sdoy_1 = oy_1.std()
        mmpyp_2 = pyp_2.mean() * ((s-g)/s) + pyp_2.median() * (g/s)
        sdpyp_2 = pyp_2.std()
        mmpy_2 = py_2.mean() * ((s-g)/s) + py_2.median() * (g/s)
        sdpy_2 = py_2.std()
        mmoyp_2 = oyp_2.mean() * ((s-g)/s) + oyp_2.median() * (g/s)
        sdoyp_2 = oyp_2.std()
        mmoy_2 = oy_2.mean() * ((s-g)/s) + oy_2.median() * (g/s)
        sdoy_2 = oy_2.std()

        mmp_1 = mmpyp_1 * ((s-g)/s) + mmpy_1 * (g/s)
        sdp_1 = sdpyp_1 * ((s-g)/s) + sdpy_1 * (g/s)
        mmo_1 = mmoyp_1 * ((s-g)/s) + mmoy_1 * (g/s)
        sdo_1 = sdoyp_1 * ((s-g)/s) + sdoy_1 * (g/s)
        mmp_2 = mmpyp_2 * ((s-g)/s) + mmpy_2 * (g/s)
        sdp_2 = sdpyp_2 * ((s-g)/s) + sdpy_2 * (g/s)
        mmo_2 = mmoyp_2 * ((s-g)/s) + mmoy_2 * (g/s)
        sdo_2 = sdoyp_2 * ((s-g)/s) + sdoy_2 * (g/s)

        ms = mmp_1.append(mmo_2).append(sdp_1).append(sdo_2).append(mmp_2).append(mmo_1).append(sdp_2).append(sdo_1)
        # }

        # Input/Sim {
        srs = pyp_1.append(oyp_1).append(pyp_2).append(oyp_2).append(py_1).append(oy_1).append(py_2).append(oy_2)
        srsp_1 = (srs.iloc[0] - srs.iloc[1]) / (s - 1)
        srsp_2 = (srs.iloc[2] - srs.iloc[3]) / (s - 1)
        srs_1 = (srs.iloc[4] - srs.iloc[5]) / g
        srs_2 = (srs.iloc[6] - srs.iloc[7]) / g

        m_1 = (srsp_1 * ((s-g)/s) + srs_1 * (g/s))
        m_2 = (srsp_2 * ((s-g)/s) + srs_2 * (g/s))
        mm_sr = m_1.append(m_2)
        m = (mm_sr.iloc[0] - mm_sr.iloc[2]) / 2
        # }

        # Sim {
        msh_1 = (ms.iloc[0] + ms.iloc[2] * 2) * .5 + (ms.iloc[1] + ms.iloc[3] * 2) * .5 + m + h_1
        msl_1 = (ms.iloc[0] - ms.iloc[2] * 2) * .5 + (ms.iloc[1] - ms.iloc[3] * 2) * .5 + m + h_1
        if msl_1 < 0:
            msl_1 = 0
        else:
            msl_1 = (ms.iloc[0] - ms.iloc[2] * 2) * .5 + (ms.iloc[1] - ms.iloc[3] * 2) * .5 + m + h_1
        msh_2 = (ms.iloc[4] + ms.iloc[6] * 2) * .5 + (ms.iloc[5] + ms.iloc[7] * 2) * .5 - m + h_2
        msl_2 = (ms.iloc[4] - ms.iloc[6] * 2) * .5 + (ms.iloc[5] - ms.iloc[7] * 2) * .5 - m + h_2
        if msl_2 < 0:
            msl_2 = 0
        else:
            msl_2 = (ms.iloc[4] - ms.iloc[6] * 2) * .5 + (ms.iloc[5] - ms.iloc[7] * 2) * .5 - m + h_2
        c = (msh_1 - msl_1 + 1) * (msh_2 - msl_2 + 1)
        # }

        # Input/Sim {
        n_1 = 0
        n_2 = 0
        if msh_2 > msh_1:
            n_2 = (msh_2 - msh_1) * (msh_1 - msl_1 + 1) + ((((msh_1 - msl_1 + 1) - 1) / 2) * (msh_1 - msl_1 + 1))
            n_1 = c - n_2 - msh_1
        elif msh_2 < msh_1:
            n_1 = (msh_1 - msh_2) * (msh_2 - msl_2 + 1) + ((((msh_2 - msl_2 + 1) - 1) / 2) * (msh_2 - msl_2 + 1))
            n_2 = c - n_1 - msh_2

        p_1 = (n_1 / c) * 100 / .95
        p_2 = (n_2 / c) * 100 / .95
        if p_1 > 100:
            p_1 = 99
            p_2 = 1
        elif p_2 > 100:
            p_2 = 99
            p_1 = 1

        m_1 = mmp_1.combine(mmo_2, max, fill_value=0)
        m_2 = mmo_1.combine(mmp_2, max, fill_value=0)
        # }

        # Sim {
        mm_1 = m_1.mean() + m + h_1
        mm_2 = m_2.mean() - m + h_2
        mm = - mm_1 + mm_2

        po = - py_1.iat[g-1, 0] + oy_1.iat[g-1, 0]
        if po < 0 and mm < 0:
            p_score_r += 1
        elif po > 0 and mm > 0:
            r_score_r += 1
        elif po < 0 and mm > 0:
            r_score_w += 1
        elif po > 0 and mm < 0:
            p_score_w += 1

        if mm < 0:
            w += 1
        elif mm > 0:
            l += 1

        g += 1
        # }

    nfl_cr[str(t_1)] = (int(w), int(l))
    # }

print(nfl_cr)
# }