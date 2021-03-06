# Create your views here.
from django.http import *
from models import *
from django.template import Context, loader
import datetime
import time


def list_open_issues(request):
    #Assumes that the CLOSED_STATUS is the middle
    issues = issue.objects.filter(status__lt=CLOSED_STATUS).order_by('updated')
    template = loader.get_template('openissues.html')
    open = issue.objects.filter(status=OPEN_STATUS)

    c = Context({
        'issues':issues,
        'oissues':len(open),
    })

    return HttpResponse (template.render(c))

def view_issue(request, issueid):
    if 1:
    #try:
        i = issue.objects.get(id = issueid)
        template = loader.get_template('issue.html')

        c = Context({
            'issue':i
        })

        return HttpResponse (template.render(c))
    #except:
    #    return HttpResponseRedirect (settings.BASE_URL)


def update_issue(request):
    if 1:
        od = request.POST['od']
        statusupdate = request.POST['su']
        issid = request.POST['id']
        mentor = request.POST['assign']
        i = issue.objects.get(id = issid)
        #i.ongoingNotes = od
        if (od != ""):
                i.initialDesc += "\n" + datetime.datetime.now().strftime("[%H:%M:%S]: ") + od
        i.ongoingNotes = ""
        i.status = int(statusupdate)
        if (mentor != i.assignedTo):
                i.initialDesc += "\n" + datetime.datetime.now().strftime("[%H:%M:%S]: Assigned mentor changed from ") + i.assignedTo + " to " + mentor
                i.assignedTo = mentor
        i.save()
        if (i.status == CLOSED_STATUS):
            return HttpResponseRedirect(settings.BASE_URL)
        else:
            return HttpResponseRedirect(settings.BASE_URL+"viewissue/"+str(i.id))
    #except:
    #return HttpResponse("bad request", status=500)

def create_issue_echoer(request):
    template = loader.get_template("createissue.html")
    context = Context ({})
    return HttpResponse(template.render(context))

def create_issue(request):
    if 1:
    #try:
        teamnumber = request.POST['tn']
        longdesc = datetime.datetime.now().strftime("[%H:%M:%S]: ")+request.POST['longdesc']
        shortdesc = request.POST['shortdesc']
        i = issue()
        i.team = teamnumber
        i.shortDesc = shortdesc
        i.initialDesc = longdesc
        i.status = OPEN_STATUS
        i.ongoingNotes = ""
        i.assignedTo = ""
        i.save()
        return HttpResponseRedirect(settings.BASE_URL+"viewissue/"+str(i.id))
    #except:
#        return HttpResponseRedirect(settings.BASE_URL+"createissueform")

def allissues(request):
    issues = issue.objects.all()
    template = loader.get_template('openissues.html')
    c = Context({
        'issues':issues
    })

    return HttpResponse (template.render(c))


def get_issue_json(request, issueid):
    #start = time.time()
    if(1):
        iss = issue.objects.get(id=int(issueid))
        json = '{"description":"%s", "assigned":"%s", "status":%d, "touched":"%s"}' % (iss.initialDesc, iss.assignedTo, iss.status, iss.updated.strftime("%H:%M:%S"))
        json = json.replace("\n", "\\n")
        #end = time.time() - start
        #json = json.replace("}", ', "time":"%d"}' % end)
        return HttpResponse(json)

