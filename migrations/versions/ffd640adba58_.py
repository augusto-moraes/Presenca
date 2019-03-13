"""empty message

Revision ID: ffd640adba58
Revises: 
Create Date: 2019-03-13 16:33:00.545522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd640adba58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('horario', sa.String(length=5), nullable=False),
    sa.Column('ID_URI', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ID_URI'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('ciclo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('data_inicio', sa.Date(), nullable=True),
    sa.Column('data_fim', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instituicao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('apelido', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('ID_URI', sa.String(length=5), nullable=True),
    sa.Column('senha', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ID_URI'),
    sa.UniqueConstraint('apelido'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('participantes',
    sa.Column('id_ciclo', sa.Integer(), nullable=False),
    sa.Column('id_instituicao', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_ciclo'], ['ciclo.id'], ),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao.id'], ),
    sa.PrimaryKeyConstraint('id_ciclo', 'id_instituicao')
    )
    op.create_table('sala',
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('capacidade', sa.Integer(), nullable=False),
    sa.Column('id_instituicao', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao.id'], ),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('aula',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dia', sa.Date(), nullable=True),
    sa.Column('horario', sa.String(length=5), nullable=False),
    sa.Column('nivel', sa.String(length=15), nullable=False),
    sa.Column('ativa', sa.Boolean(), server_default=sa.text('0'), nullable=False),
    sa.Column('id_prof', sa.Integer(), nullable=True),
    sa.Column('sala', sa.String(length=30), nullable=True),
    sa.Column('ciclo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ciclo'], ['ciclo.id'], ),
    sa.ForeignKeyConstraint(['id_prof'], ['professor.id'], ),
    sa.ForeignKeyConstraint(['sala'], ['sala.nome'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('presenca',
    sa.Column('id_aula', sa.Integer(), nullable=False),
    sa.Column('id_aluno', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_aluno'], ['aluno.id'], ),
    sa.ForeignKeyConstraint(['id_aula'], ['aula.id'], ),
    sa.PrimaryKeyConstraint('id_aula', 'id_aluno')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presenca')
    op.drop_table('aula')
    op.drop_table('sala')
    op.drop_table('participantes')
    op.drop_table('professor')
    op.drop_table('instituicao')
    op.drop_table('ciclo')
    op.drop_table('aluno')
    # ### end Alembic commands ###
