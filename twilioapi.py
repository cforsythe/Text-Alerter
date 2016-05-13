from flask import Flask, request, redirect
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE
import twilio.twiml
import gmaps

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    body = str(request.form['Body'])
    if body.lower() == 'pls dont do this I hate you':
        resp = twilio.twiml.Response()
        resp.message("We hate you too")
        return str(resp)
    else:
        write = True
        filename = 'whitelist.txt'
        fnumber = str(request.form['From'])
        tnumber = str(request.form['To'])
        incoming = str("To: " + tnumber + " From: " + fnumber + "\n")

        with open(filename) as f:
            for line in f:
                print incoming
                print line
                line = str(line)
                if line == incoming:
                    write = False

        if body.lower() == 'pls verify':
            phonelist = open(filename, 'a')
            phonelist.write("To: " + tnumber + " From: " + fnumber + "\n")
            phonelist.close()
            Popen([executable, 'quickstart.py'], creationflags=CREATE_NEW_CONSOLE)
            resp = twilio.twiml.Response()
            resp.message("You have been verified, you will now receive alerts for your Google Calendar events")
            return str(resp)
        if body.lower() == 'pls dont':
            resp = twilio.twiml.Response()
            resp.message("We will not verify you")
            return str(resp)

        if write == True:
            resp = twilio.twiml.Response()
            resp.message("You are not on our Whitelist would you like to Verify? Responses are 'pls verify' and 'pls dont' ")
            return str(resp)






        """Respond to incoming calls with a simple text message."""
        print body
        if write == False:
            if body.lower() == 'hello':
                resp = twilio.twiml.Response()
                resp.message("Nice you found an easter egg :), Hello to you!")
                return str(resp)
            if body.lower() == 'directions':
                resp = twilio.twiml.Response()
                resp.message("Text us     'S: #startlocation            D: #endlocation' and we will send directions")
                return str(resp)
            if 's:' in body.lower():
                startbegin = 's:'
                endbegin = 'd:'

                beginindex = body.lower().find(startbegin) + 2    ###getting locations out of text body
                endindex = body.lower().find(endbegin)
                startlocation = body[beginindex:endindex]
                endlocation = body[endindex+2:]

                directions = gmaps.directions(startlocation,endlocation)

                steps = len(directions)
                finaldir = ''
                for i in range(1,steps):
                    finaldir += '\n' + str(i) + ". " + directions[i] + '\n'
                resp = twilio.twiml.Response()
                resp.message(finaldir)
                return str(resp)
            else:
                resp = twilio.twiml.Response()
                resp.message("Sorry, we dont know what to say :(")
                return str(resp)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='80')
