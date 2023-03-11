from pycalc.operations import operations
import click

@click.command()
@click.option('--num1', help='First Number', prompt='Enter first number', type=int)
@click.option('--num2', help='Second Number', prompt='Enter second number', type=int)
@click.option('--opr', help='Operation', prompt='Enter operation type')

def main(num1, num2, opr):
    opr_o = operations()
    opr_o.num1 = num1
    opr_o.num2 = num2
    if(opr == 'add'):
        print(f'Sum : {opr_o.sum()}')

if __name__ == '__main__':
    main()
