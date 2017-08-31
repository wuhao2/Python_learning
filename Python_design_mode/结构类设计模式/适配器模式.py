# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 9:21'
'''
外包人员系统兼容 假设某公司A与某公司B需要合作，公司A需要访问公司B的人员信息，
但公司A与公司B协议接口不同，该如何处理？
先将公司A和公司B针对各自的人员信息访问系统封装了对象接口。
'''


class ACpnStaff:
    name = ""
    id = ""
    phone = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print("A protocol getName method...id:%s" % self.id)
        return self.name

    def setName(self, name):
        print("A protocol setName method...id:%s" % self.id)
        self.name = name

    def getPhone(self):
        print("A protocol getPhone method...id:%s" % self.id)
        return self.phone

    def setPhone(self, phone):
        print("A protocol setPhone method...id:%s" % self.id)
        self.phone = phone


class BCpnStaff:
    name = ""
    id = ""
    telephone = ""

    def __init__(self, id):
        self.id = id

    def get_name(self):
        print("B protocol get_name method...id:%s" % self.id)
        return self.name

    def set_name(self, name):
        print("B protocol set_name method...id:%s" % self.id)
        self.name = name

    def get_telephone(self):
        print("B protocol get_telephone method...id:%s" % self.id)
        return self.telephone

    def set_telephone(self, telephone):
        print("B protocol get_name method...id:%s" % self.id)
        self.telephone = telephone

'''
适配器类
适配器可以认为是对现在业务的补偿式应用，
所以，尽量不要在设计阶段使用适配器模式，
在两个系统需要兼容时可以考虑使用适配器模式。
'''
class CpnStaffAdapter:
    b_cpn = ""

    def __init__(self, id):
        self.b_cpn = BCpnStaff(id)

    def getName(self):
        return self.b_cpn.get_name()

    def getPhone(self):
        return self.b_cpn.get_telephone()

    def setName(self, name):
        self.b_cpn.set_name(name)

    def setPhone(self, phone):
        self.b_cpn.set_telephone(phone)


if __name__ == "__main__":
    acpn_staff = ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print("A Staff Name:%s" % acpn_staff.getName())
    print("A Staff Phone:%s" % acpn_staff.getPhone())
    bcpn_staff = CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print("B Staff Name:%s" % bcpn_staff.getName())
    print("B Staff Phone:%s" % bcpn_staff.getPhone())
