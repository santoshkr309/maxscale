import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
confd_template = env.get_template('/tmp/maxscale/component_subcomponent_template.cnf')
cnf_template = env.get_template('/tmp/maxscale/maxscale.cnf')
values = yaml.safe_load(open('/tmp/maxscale/templates/mx-component.yaml'))

for service in values["onboarded_components"]:
    file=open(service['component']+"_"+service['subcomponent']+".cnf", "w")
    file.write(confd_template.render(service))
    file.close()

file = open("/tmp/maxscale/templates/maxscale.cnf","w")
server_csv = []
for server in values["onboarded_components"]:
    server_csv.append("server-"+server['component']+'_'+server['subcomponent'])

servers_csv = ','.join(server_csv)
file.write(cnf_template.render(servers_csv=servers_csv))
file.close()
