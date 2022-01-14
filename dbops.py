from datetime import datetime
import json, sys, sqlite3
from flask import jsonify


class DBSimple():
    @staticmethod
    def nicknames():
        dbpath = "malone.db"
        sql = """select nickname from Users"""
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        conn.close()
        print(result)
        return result


class DBFriend():
    def __init__(self):
        self.timeStamp = datetime.now()
        self.dbpath = "malone.db"


    def doStuff(self, sql, var, returnMessage, failMessage):
        try:
            conn = sqlite3.connect(self.dbpath)
            cur = conn.cursor()
            cur.execute(sql, var)
            conn.commit()
            conn.close()
            print("Success", file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)

    def getStuff(self, sql, var = None):
        failMessage = "Problem connecting to database"
        try:
            conn = sqlite3.connect(self.dbpath)
            cur = conn.cursor()
            if var == None:
                cur.execute(sql)
                columns = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                result = []
                for row in rows:
                    row = dict(zip(columns, row))
                    result.append(row)
                conn.close()
                return result
            else:
                cur.execute(sql, var)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                result = []
                for row in rows:
                    row = dict(zip(columns, row))
                    result.append(row)
                conn.close()
                return result
        except Exception as e:
            print(e)
            return ({"id":failMessage})
    def nicknames(self):
        sql = """select nickname from Users"""
        var = None
        results = self.getStuff(sql, var)
        return results

    def choreCount(self):
        sql = """select count(chore_id) from Chores where completed_date is null"""
        try:
            conn = sqlite3.connect(self.dbpath)
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchone()[0]
            conn.close()
            return result
        except:
            return '0'

    def openChores(self):
        sql = """select ch.chore_id as 'id'
                , ch.name as 'name'
                , ch.description as 'description'
                , ch.chore_id
                , u.nickname as 'nickname'
                , u.first as 'first'
                , u.last as 'last'
                , ch.due_date as 'due'
                from Chores ch
                left outer join Users u
                    on u.user_id = ch.person
                where completed_date is null"""
        var = None
        results = self.getStuff(sql, var)
        return results

    def createChores(self, name, description):
        now = datetime.now()
        var = (name, description, now, now)
        #hard coded to no one
        sql = """insert into Chores
                (name, description, person, entry_date
                , due_date, approved, completed_date)
                values(?, ?, 5, ?, ?, 0, null)

                """
        output =  self.doStuff(sql, var, "Chore Created", "Could not create chore")
        return output

    def completeChores(self, chore_id):
        now = datetime.now()
        var = (now, chore_id)
        sql = """update Chores
                    set completed_date = ?
                    where chore_id = ?"""
        return self.doStuff(sql, var, "Chore Completed", "Could not complete chore")
    def deleteChore(self, chore_id):
        sql = "delete from Chores where chore_id =" + str(chore_id)
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
