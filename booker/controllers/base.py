from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

from booker import lib

VERSION_BANNER = get_version()


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Application for calculating book pages for printing'

        # text displayed at the bottom of --help output
        epilog = 'Usage: booker calc --foo bar'

        # controller level arguments. ex: 'booker --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='calculate pages to print ',

        # sub-command level arguments. ex: 'booker command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-p', '--pages' ],
              { 'help' : 'number of pages in book',
                'action'  : 'store',
                'type' : int,
                'dest' : 'pages' } ),
            ( [ '-s', '--sheets' ],
              { 'help' : 'number of sheets in a block',
                'action'  : 'store',
                'type' : int,
                'dest' : 'sheets' } ),
        ],
        
    )
    def calc(self):
        if self.app.pargs.pages is not None and self.app.pargs.sheets is not None:
            #if type(self.app.pargs.pages) is int and self.app.pargs.sheets is int:
            data = dict()
            data['calculated_pages'] = lib.calculate_pages(self.app.pargs.pages, self.app.pargs.sheets)
            import pprint 
            pprint.pprint(data['calculated_pages'])
            
            #TODO: доделать нормальный рендер через шаблон
            #self.app.render(data, 'calc.jinja2')
