from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
@app.route("/home",methods=["GET", "POST"])
def home():
    M=[['','']]*10
    T=[['','']]*10
    W=[['','']]*10
    TH=[['','']]*10
    F=[['','']]*10
    tt={'M':M,'T':T,'W':W,'TH':TH,'F':F}
    if request.method == 'POST':
        data=request.form
        if data['shift']== 'MORNING':
            M[1]=TH[3]=F[2]=[data['A'],"#ff9dff"]
            if data['A']:
                W[4]=[data['A']+'(+)',"#ff9dff"]
            M[2]=T[1]=F[3]=[data['B'],'yellow']
            if data['B']:
                TH[4]=[data['B']+'(+)','yellow']
            M[3]=T[2]=W[1]=[data['C'],'#8afdfa']
            if data['C']:
                F[4]=[data['C']+'(+)','#8afdfa']
            T[3]=W[2]=TH[1]=[data['D'],'#ffa750']
            if data['D']:
                M[4]=[data['D']+'(+)','#ffa750']
            W[3]=TH[2]=F[1]=[data['E'],'#FFCEFE']
            if data['E']:
                T[4]=[data['E']+'(+)','#FFCEFE']
            M[0]=T[9]=TH[0]=[data['F'],'#9D3C72']
            if data['F']:
                F[9]=[data['F']+'(+)','#9D3C72']
            M[9]=W[0]=TH[9]=[data['G'],'#FAD6A5']
            T[0]=W[9]=F[0]=[data['H'],'#03C988']
            if data['P']:
                M[6]=M[8]=[' ','palegreen']
                M[7]=[data['P'],'palegreen']
            if data['Q']:
                T[6]=T[8]=[' ','palegreen']
                T[7]=[data['Q'],'palegreen']
            if data['R']:
                W[6]=W[8]=[' ','palegreen']
                W[7]=[data['R'],'palegreen']
            if data['S']:
                TH[6]=TH[8]=[' ','palegreen']
                TH[7]=[data['S'],'palegreen']
            if data['T']:
                F[6]=F[8]=[' ','palegreen']
                F[7]=[data['T'],'palegreen']
        if data['shift']== 'AFTERNOON':
            M[6]=TH[8]=F[7]=[data['A'],"#ff9dff"]
            if data['A']:
                W[5]=[data['A'],"#ff9dff"]
            M[7]=T[6]=F[8]=[data['B'],'yellow']
            if data['B']:
                TH[5]=[data['B']+'(+)','yellow']
            M[8]=T[7]=W[6]=[data['C'],'#8afdfa']
            if data['C']:
                F[5]=[data['C']+'(+)','#8afdfa']
            T[8]=W[7]=TH[6]=[data['D'],'#ffa750']
            if data['D']:
                M[5]=[data['D']+'(+)','#ffa750']
            W[8]=TH[7]=F[6]=[data['E'],'#FFCEFE']
            if data['E']:
                T[5]=[data['E']+'(+)','#FFCEFE']
            M[0]=T[9]=TH[0]=[data['F'],'#9D3C72']
            if data['F']:
                F[9]=[data['F']+'(+)','#9D3C72']
            M[9]=W[0]=TH[9]=[data['G'],'#FAD6A5']
            T[0]=W[9]=F[0]=[data['H'],'#03C988']
            if data['P']:
                M[1]=M[3]=[' ','palegreen']
                M[2]=[data['P'],'palegreen']
            if data['Q']:
                T[1]=T[3]=[' ','palegreen']
                T[2]=[data['Q'],'palegreen']
            if data['R']:
                W[1]=W[3]=[' ','palegreen']
                W[2]=[data['R'],'palegreen']
            if data['S']:
                TH[1]=TH[3]=[' ','palegreen']
                TH[2]=[data['S'],'palegreen']
            if data['T']:
                F[1]=F[3]=[' ','palegreen']
                F[2]=[data['T'],'palegreen']
        tt['M']=M
        tt['T']=T
        tt['W']=W
        tt['TH']=TH
        tt['F']=F
        
    return render_template('home.html',tt=tt)


if __name__ == '__main__':
    app.run(debug=True)